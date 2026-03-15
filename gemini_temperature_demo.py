from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

prompt = "Explain photosynthesis as if you are a pirate teaching a classroom of children in one paragraph."

temps = [0.2, 0.7, 1.0]

for t in temps:
    print("\n----------------------------")
    print(f"Temperature: {t}")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=t
            
        )
    )

    print(response.text)