# app/agents/diagnosis_agent.py

from app.tools.symptom_extractor import extract_symptoms
from app.tools.pubmed_fetcher import search_pubmed
from app.prompts.medical_prompts import DIAGNOSIS_REASONING_PROMPT
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class DiagnosisAgent:
    def __init__(self):
        self.name = "Medical Research Assistant"

    def run(self, user_description: str):
        # 1. Extract Entities
        print(f"--- Extracting symptoms from: {user_description[:30]}... ---")
        extracted_data = extract_symptoms(user_description)
        symptoms = extracted_data.get("entities", {}).get("symptoms", [])

        # 2. Search PubMed using the first 2 symptoms found
        search_query = "+".join(symptoms[:2])
        print(f"--- Searching PubMed for: {search_query} ---")
        research_papers = search_pubmed(search_query)

        # 3. Final Reasoning (The Brain brings it all together)
        print("--- Generating Final Report ---")
        
        # Prepare the context for the LLM
        context = f"""
        Patient Symptoms: {extracted_data}
        Related Research: {research_papers}
        """

        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": DIAGNOSIS_REASONING_PROMPT},
                {"role": "user", "content": context}
            ]
        )

        return response.choices[0].message.content