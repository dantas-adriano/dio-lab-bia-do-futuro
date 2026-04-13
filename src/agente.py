import pandas as pd
import google.generativeai as genai
from config import MODELO

# System Prompt oficial do JULLIUS
SYSTEM_PROMPT = """Você é JULLIUS, um assistente financeiro especializado em ajudar usuários a controlar seus gastos.

OBJETIVO:
- Monitorar transações e identificar padrões de consumo.
- Emitir alertas curtos e diretos quando gastos ultrapassarem limites pré-definidos.
- Sugerir metas simples de economia de forma preventiva.
- Comunicar-se em tom informal e acessível, usando linguagem clara e próxima do cotidiano.
- Nunca inventar dados: use apenas informações fornecidas pelo usuário ou pela base de conhecimento.
- Não oferecer recomendações de investimento ou crédito.
"""

# Função para carregar transações
def carregar_transacoes():
    df = pd.read_csv("./data/transacoes.csv")
    return df

# Função para perguntar ao modelo Gemini
def perguntar(mensagem, contexto_extra=""):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto_extra}

Pergunta: {mensagem}
"""
    model = genai.GenerativeModel(MODELO)
    response = model.generate_content(prompt)
    return response.text
    


