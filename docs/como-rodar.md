# 🚀 Como Rodar o Projeto JULLIUS

## 1. Criar o ambiente virtual (venv)
No terminal do VS Code, dentro da pasta raiz do projeto:

```bash
python -m venv venv
```

Isso cria a pasta `venv` com o ambiente virtual.

---

## 2. Ativar o venv
Dependendo do sistema operacional:

- **Windows (PowerShell ou terminal do VS Code):**
```powershell
venv\Scripts\activate
```

- **Linux/Mac (bash/zsh):**
```bash
source venv/bin/activate
```

Se deu certo, você verá `(venv)` no início da linha do terminal.

---

## 3. Instalar dependências
Com o venv ativo, rode:

```bash
pip install -r src/requirements.txt
```

Isso instala todas as bibliotecas necessárias (`streamlit`, `pandas`, `requests`, `google-generativeai`).

---

## 4. Configurar a API Key do Gemini
No Windows (PowerShell), defina a variável de ambiente:

```powershell
$env:GOOGLE_API_KEY="SUA_CHAVE_AQUI"
```

No Linux/Mac:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
```

> Dica: se preferir, você pode colocar a chave diretamente no `config.py` para testes.

---

## 5. Rodar a aplicação
Execute:

```bash
streamlit run src/app.py
```

O Streamlit abrirá no navegador (geralmente em `http://localhost:8501`).

---

## 6. Testar o agente JULLIUS
Digite perguntas como:
- "Quanto gastei em restaurantes este mês?"  
- "Quero economizar R$ 200, como faço?"  
- "Me avise se passar de R$ 100 em transporte."  

O agente deve responder com base no **system prompt** e nos dados do `transacoes.csv`.

---

👉 Agora você tem um guia prático para rodar o projeto sempre que precisar.  

Quer que eu também prepare um **roteiro de testes práticos** (lista de perguntas organizadas por cenários e edge cases) para validar se o JULLIUS está funcionando conforme o esperado?
