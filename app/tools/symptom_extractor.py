import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_symptoms(user_input: str):
    """
    Takes raw text and returns a dictionary of medical entities.
    Example: "I've had a sharp headache for 3 days, it's an 8/10 pain."
    """
    from app.prompts.medical_prompts import SYMPTOM_EXTRACTION_PROMPT

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": SYMPTOM_EXTRACTION_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={ "type": "json_object" } # Forces the AI to return valid JSON
    )

    # Convert the string response back into a Python Dictionary
    return json.loads(response.choices[0].message.content)