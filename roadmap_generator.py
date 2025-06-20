from transformers import pipeline

def generate_roadmap(user_data):
    prompt = f"""
    Based on this coding profile:\n\n{user_data}\n\n
    Suggest an action plan for the next 2 weeks, focusing on:
    - Weak topics
    - Competitive programming contests
    - Interview prep questions
    Provide bullet points.
    """
    generator = pipeline("text-generation", model="Salesforce/codet5-base")
    result = generator(prompt, max_length=300, do_sample=True, temperature=0.7)
    return result[0]['generated_text']
