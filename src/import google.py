import google.generativeai as genai

genai.configure(api_key="SUA_CHAVE_AQUI")

for m in genai.list_models():
    print(m.name)
