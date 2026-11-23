import os
from google import genai

def extract_query(description):

    client = genai.Client(api_key=os.getenv("GOOGLE_KEY"))

    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        system_instruction="Extract a search query from the following description for product search containing the relevant features and adjectives.",
        input=f"Here is the description of the product I am searching for: '{description}'",
        generation_config={
            "thinking_level": "low",
            "temperature": 0
        }
    )

    print(f"The LLM returned the following response: {interaction.output_text}")
    return interaction.output_text