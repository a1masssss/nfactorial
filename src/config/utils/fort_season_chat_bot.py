import openai
import time
import os 
client = openai.OpenAI(api_key = os.getenv('OPEN_API_KEY'))
def history_tolc(chapter: int, season: int, user_prompt: str):
    system_prompt = f"""
    You have good knowledge in each Fortnite seasons and chapters!
    You gonna tolc about chapter {chapter} and season {season} in Fortnite.
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

