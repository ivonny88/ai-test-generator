from groq import Groq
import os
from src.prompts import TEST_GENERATION_PROMPT, sanitize_input
from dotenv import load_dotenv

load_dotenv()

def generate_test_cases(feature_description: str) -> str:
    """
    Generates pytest test cases from a feature description using Groq API.
    
    Args:
        feature_description: Text describing the feature to test
        
    Returns:
        String containing generated pytest code
    """
    # Sanitize input before sending to the model
    clean_input = sanitize_input(feature_description)

    if not clean_input:
        return "# Error: Please provide a valid feature description."

    if clean_input == "INVALID_INPUT":
        return "# Error: Invalid input detected. Please describe a software feature to test."

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": TEST_GENERATION_PROMPT
            },
            {
                "role": "user",
                "content": f"Feature to test:\n{clean_input}"
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content