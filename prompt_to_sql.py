from transformers import pipeline
from accelerate import Accelerator
import torch

accelerator = Accelerator()

@accelerator.on_main_process
def load_model():
    return pipeline("text2text-generation", 
                   model="tscholak/text-to-sql",
                   device_map="auto",
                   torch_dtype=torch.float16)

def prompt_to_sql(prompt):
    full_prompt = f"""
    Convert to SQL: {prompt}
    Schema: users(id,name,signup_date), products(id,name,sales)
    """
    
    with accelerator.local_main_process_first():
        generator = load_model()
        return generator(full_prompt, max_length=500)[0]['generated_text']
