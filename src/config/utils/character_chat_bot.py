import openai
import os
import time

client = openai.OpenAI(api_key = os.getenv('OPEN_API_KEY'))

def ai_tolc(fort_character: str, user_prompt: str):
    system_prompt = f"""
    Imagine you are {fort_character}, a Fortnite character.
    Respond to the user as if you are {fort_character} — stay in character, use their tone and style.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            stream=True
        )
        
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                yield f"data: {content}\n\n"
                time.sleep(0.01)
        
        yield "data: [DONE]\n\n"

    except Exception as e:
        print(f"OpenAI API Error: {str(e)}")
