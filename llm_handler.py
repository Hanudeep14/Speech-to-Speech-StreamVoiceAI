import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def get_llm_response(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
