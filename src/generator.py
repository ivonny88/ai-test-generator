from groq import Groq
import os
from src.prompts import TEST_GENERATION_PROMPT
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
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"{TEST_GENERATION_PROMPT}\\n\\nFeature to test:\\n{feature_description}"
            }
        ],
        max_tokens=1000
    )
    
    return response.choices[0].message.content