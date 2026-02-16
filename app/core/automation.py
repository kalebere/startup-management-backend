import os
from typing import List

from google import genai
from google.genai.types import GenerateContentConfig


# -------------------------
# Configuration
# -------------------------

API_KEY = "AIzaSyCwtTGEnLbd1ntiSU8rlry9CwU0EsKE7m0"

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3-flash-preview"

# -------------------------
# LLM Chain
# -------------------------

class LLMChain:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.context_history: List[str] = []

    def add_context(self, context: str) -> None:
        self.context_history.append(context)

    def build_prompt(self, user_input: str) -> str:
        context_block = "\n".join(self.context_history)

        return f"""
SYSTEM INSTRUCTION:
{self.system_prompt}

MANUAL CONTEXT:
{context_block}

USER QUERY:
{user_input}

Respond precisely and technically.
""".strip()

    def run(self, user_input: str) -> str:
        prompt = self.build_prompt(user_input)

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



if __name__ == "__main__":

    chain = LLMChain(
        system_prompt="You are a senior backend architect. Provide structured answers."
    )

    result = chain.run(
        "How should I design a scalable authentication service?"
    )

    print(result)
