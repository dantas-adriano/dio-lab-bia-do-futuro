# Código da Aplicação - JULLIUS

Esta pasta contém o código do JULLIUS, um agente financeiro inteligente que ajuda usuários a monitorar gastos e definir metas de economia de forma simples e acessível.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (interface Streamlit)
├── agente.py           # Lógica do agente e interação com o modelo Gemini
├── config.py           # Configurações (API Key, modelo, etc.)
└── requirements.txt    # Lista de dependências
```

## Exemplo de requirements.txt

```
streamlit
pandas
google-generativeai
```

## Como Rodar

```bash
# Criar ambiente virtual (venv):
python -m venv venv

# Ativar o venv:
  # - Windows (PowerShell):
  venv\Scripts\activate
  # - Linux/Mac:
  source venv/bin/activate

# Instalar dependências:
pip install -r requirements.txt

# Configurar a API Key do Gemini:
  # - Windows (PowerShell):
  $env:GOOGLE_API_KEY="SUA_CHAVE_AQUI"
  # - Linux/Mac:
  export GOOGLE_API_KEY="SUA_CHAVE_AQUI"

# Rodar a aplicação:
streamlit run src/app.py
```

🎯 Objetivo do JULLIUS
- Monitorar transações e identificar padrões de consumo.
- Emitir alertas quando gastos ultrapassarem limites.
- Sugerir metas simples de economia.
- Comunicar-se em tom informal e acessível.
- Nunca inventar dados: usar apenas informações fornecidas pelo usuário.
