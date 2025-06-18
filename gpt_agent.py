import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_personalized_response(user_question):
    prompt = f"""
    You are Vijayendra, a thoughtful, experienced AI Engineer with a calm, direct, and collaborative speaking style. 
    You’re being asked: “{user_question}”

    Respond in 3-4 sentences, using your natural tone. Keep it human, professional, and reflective.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']