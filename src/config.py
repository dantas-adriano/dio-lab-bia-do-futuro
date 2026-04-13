import os
import google.generativeai as genai

# Configure sua API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Modelo Gemini
MODELO = "models/gemini-2.5-flash-lite"

