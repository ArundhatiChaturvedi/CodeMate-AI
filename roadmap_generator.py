from transformers import pipeline
from accelerate import Accelerator
import torch
import re
import json

accelerator = Accelerator()

@accelerator.on_main_process
def load_model():
    return pipeline("text-generation", 
                   model="Salesforce/codet5-base",
                   device_map="auto",
                   torch_dtype=torch.float16)

def generate_roadmap(user_data):
    prompt = f"""
    Analyze this coding profile: {user_data}
    
    Task 1: Extract top 5 programming topics covered. Format as JSON: {{"topics": ["topic1", ...]}}
    
    Task 2: Create a comprehensive 2-week action plan with:
    - Clear daily goals
    - Topic-specific practice recommendations
    - Contest preparation strategies
    - Interview prep milestones
    
    Format Task 2 as markdown with sections:
    # 2-Week Action Plan
    ## Weak Topics
    - [Topic 1]: 5 problems
    - [Topic 2]: 3 problems
    ## Contest Preparation
    - [Contest Name]: Preparation strategy
    ## Interview Prep
    - Daily schedule
    - Mock interview schedule
    """
    
    with accelerator.local_main_process_first():
        generator = load_model()
        result = generator(prompt, max_length=2048, do_sample=True, temperature=0.5)[0]['generated_text']
        
        # Extract both components
        topics = ["Data Structures", "Algorithms"]  
        detailed_plan = "Could not generate detailed plan"  
        
        try:
            # Extract JSON topics
            json_match = re.search(r'{\s*"topics"\s*:\s*\[.*?\]\s*}', result, re.DOTALL)
            if json_match:
                topics = json.loads(json_match.group())["topics"]
            
            # Extract markdown plan
            plan_match = re.search(r'# 2-Week Action Plan(.+?)(?=\n#|\Z)', result, re.DOTALL)
            if plan_match:
                detailed_plan = f"# 2-Week Action Plan{plan_match.group(1)}"
        
        except Exception as e:
            print(f"Roadmap parsing error: {e}")
        
        return {
            "topics": topics[:5], 
            "detailed_plan": detailed_plan
        }
