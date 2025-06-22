from transformers import pipeline
from accelerate import Accelerator
import torch

accelerator = Accelerator()

@accelerator.on_main_process
def load_model():
    return pipeline("text-generation", 
                   model="Salesforce/codegen-350M-mono",  
                   device_map="cpu")

def prompt_to_code(prompt):
    with accelerator.local_main_process_first():
        generator = load_model()
        return generator(prompt, max_length=1024, do_sample=True, temperature=0.7)[0]['generated_text']
