import streamlit as st
from agente import perguntar, carregar_transacoes

st.title("💸 JULLIUS - Assistente de Controle de Gastos")

# Carregar transações mockadas
transacoes = carregar_transacoes()

st.write("### Últimas transações registradas")
st.dataframe(transacoes)

# Interface de chat
if pergunta := st.chat_input("Digite sua dúvida sobre seus gastos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("JULLIUS está analisando..."):
        resposta = perguntar(pergunta, contexto_extra=transacoes.to_string(index=False))

        # 🔧 Ajustes de formatação:
        # 1. Forçar parágrafos
        resposta = resposta.replace("\n", "\n\n")
        # 2. Normalizar espaços
        resposta = " ".join(resposta.split())

        # 3. Adicionar cabeçalho e emojis para dar mais clareza
        resposta_formatada = f"""
👋 **JULLIUS responde:**

{resposta}

---

🎯 **Meta final:** Foque em pequenas mudanças para atingir sua economia!
"""

        # Exibir como Markdown para manter negrito, listas e emojis
        st.chat_message("assistant").markdown(resposta_formatada, unsafe_allow_html=True)
