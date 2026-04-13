# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Para validar o agente JULLIUS, foram realizados testes práticos com diferentes tipos de perguntas. Todos os cenários tiveram resultado positivo:

### Teste 1: Consulta de gastos por categoria
- Pergunta: "Quanto gastei com alimentação?"
- Resposta esperada: Valor calculado a partir do transacoes.csv.
- Resultado: ✅ Correto — o agente retornou o valor exato e contextualizou o gasto.

### Teste 2: Definição de meta de economia
- Pergunta: "Quero economizar R$200 por mês."
- Resposta esperada: Sugestões práticas de cortes em categorias relevantes.
- Resultado: ✅ Correto — o agente analisou transações e sugeriu reduções em restaurantes, transporte e entretenimento.

### Teste 3: Pergunta fora do escopo
- Pergunta: "Qual a previsão do tempo?"
- Resposta esperada: O agente informa que só trata de finanças.
- Resultado: ✅ Correto — o agente recusou responder e manteve o foco em finanças pessoais.

### Teste 4: Solicitação de informação inexistente
- Pergunta: "Quanto rende o produto XYZ?"
- Resposta esperada: O agente admite não ter essa informação.
- Resultado: ✅ Correto — o agente respondeu de forma segura, sem inventar dados.

---

## Resultados

**O que funcionou bem:**
- Assertividade: O agente respondeu corretamente às perguntas sobre gastos e metas.
- Segurança: Evitou inventar informações e manteve o escopo restrito a finanças pessoais.
- Coerência: As respostas foram contextualizadas com base nos dados do usuário, em tom informal e acessível.
- Visual: Implementamos melhorias na formatação das respostas, como uso de negrito, listas, emojis e separação em blocos, tornando a leitura mais clara e envolvente.

**O que pode melhorar:**
- Formatação avançada: Evoluir a apresentação das respostas com subtítulos por categoria (ex.: “🍽️ Restaurantes”, “🚗 Transporte”), tabelas simples ou destaques visuais para metas.
- Personalização contínua: Ajustar o tom e as sugestões conforme o histórico do usuário, tornando o agente ainda mais adaptado ao perfil individual.
- Feedback interativo: Permitir que o usuário confirme ou ajuste as metas sugeridas diretamente na interface, criando um ciclo de interação mais dinâmico.

