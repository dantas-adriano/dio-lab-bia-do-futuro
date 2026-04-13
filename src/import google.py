import google.generativeai as genai

genai.configure(api_key="AIzaSyCJsvQSlEqLwqrLgjBwouzg55XoS7XglXo")

for m in genai.list_models():
    print(m.name)
