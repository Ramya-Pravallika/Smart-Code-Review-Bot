import openai
from .prompts import review_prompt

def get_ai_feedback(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior code reviewer."},
            {"role": "user", "content": review_prompt.format(code=code)}
        ]
    )
    return [response['choices'][0]['message']['content']]