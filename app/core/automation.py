import os
from typing import List

from google import genai
from google.genai.types import GenerateContentConfig


API_KEY = "AIzaSyCwtTGEnLbd1ntiSU8rlry9CwU0EsKE7m0"

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3-flash-preview"


class LLMChain:
    system_prompt = "You Are the most senior project manager and owner."
    user_prompt = ""

    @staticmethod
    def main_run(user_input: str) -> str:
        LLMChain.user_prompt = user_input
        prompt = f"""
            SYSTEM INSTRUCTION:
            {LLMChain.system_prompt}

            MANUAL CONTEXT:
            give me summary of the roadmap, required technical skills, estimate time and budget for the given domain as user query.

            USER QUERY:
            {LLMChain.user_prompt}

            Respond precisely and technically.
            """.strip()

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=GenerateContentConfig(
                    temperature=0.2,
                    top_p=0.9,
                    max_output_tokens=1024,
                ),
            )

            return response.text or ""

        except Exception as e:
            return f"Model error: {str(e)}"
        
    @staticmethod
    def generate_roadmap(user_input: str) -> str:
        prompt = f"""
            SYSTEM INSTRUCTION:
            {LLMChain.system_prompt}

            MANUAL CONTEXT:
            Generate Detailed Roadmap for the given domain as user query.

            USER QUERY:
            {LLMChain.user_prompt}

            Respond precisely and technically.
            """.strip()

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=GenerateContentConfig(
                    temperature=0.2,
                    top_p=0.9,
                    max_output_tokens=1024,
                ),
            )

            return response.text or ""

        except Exception as e:
            return f"Model error: {str(e)}"
    
    @staticmethod
    def required_skill(user_input: str) -> str:
        prompt = f"""
            SYSTEM INSTRUCTION:
            {LLMChain.system_prompt}
    
            MANUAL CONTEXT:
            Give me Required technical Skills in detail for the given domain as user query.

            USER QUERY:
            {LLMChain.user_prompt}

            Respond precisely and technically.
            """.strip()

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=GenerateContentConfig(
                    temperature=0.2,
                    top_p=0.9,
                    max_output_tokens=1024,
                ),
            )

            return response.text or ""

        except Exception as e:
            return f"Model error: {str(e)}"
        
    @staticmethod
    def time_and_budget_prediction(user_input: str) -> str:
        prompt = f"""
            SYSTEM INSTRUCTION:
            {LLMChain.system_prompt}
    
            MANUAL CONTEXT:
            Give me time and budget in detail for the given domain as user query.

            USER QUERY:
            {LLMChain.user_prompt}

            Respond precisely and technically.
            """.strip()

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=GenerateContentConfig(
                    temperature=0.2,
                    top_p=0.9,
                    max_output_tokens=1024,
                ),
            )

            return response.text or ""

        except Exception as e:
            return f"Model error: {str(e)}"