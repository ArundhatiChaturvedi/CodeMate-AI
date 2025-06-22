from transformers import pipeline
import torch
from accelerate import Accelerator

accelerator = Accelerator()

@accelerator.on_main_process
def load_model():
    return pipeline("text-generation", 
                   model="Salesforce/codegen-350M-mono",  
                   device_map="cpu")

def review_code_as_senior(code, context=None):
    prompt = f"""
    As senior developer, review this code:
    {code}
    {f"Context: {context}" if context else ""}
    Focus on:
    - Security vulnerabilities
    - Performance optimizations
    - Code smells
    - Best practices
    Structure feedback with bullet points.
    """
    
    with accelerator.local_main_process_first():
        generator = load_model()
        feedback = generator(prompt, max_length=1024, do_sample=True, temperature=0.5)[0]['generated_text']
        return feedback.split("Focus on:")[-1].strip()
