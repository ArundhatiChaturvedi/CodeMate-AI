from transformers import pipeline

def prompt_to_code(prompt):
    generator = pipeline("text-generation", model="Salesforce/codegen2-1B")
    output = generator(prompt, max_length=256, do_sample=True, temperature=0.7)
    return output[0]['generated_text']
