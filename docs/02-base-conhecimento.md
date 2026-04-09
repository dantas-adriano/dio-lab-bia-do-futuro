# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores (ex.: evitar repetição de respostas) |
| `perfil_investidor.json` | JSON | Não utilizado neste agente (focado apenas em controle de gastos) |
| `produtos_financeiros.json` | JSON | Não utilizado neste agente |
| `transacoes.csv` | CSV | Principal fonte de dados: análise de padrão de gastos do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O arquivo transacoes.csv foi substituído por uma versão mockada criada especificamente para este projeto.
Essa versão contém categorias como Alimentação, Transporte, Entretenimento, Restaurantes, Saúde e Compras, com valores simulados para um mês de transações.
Essa adaptação permite que o agente JULLIUS:
- Some gastos por categoria.
- Compare com limites pré-definidos.
- Gere alertas quando ultrapassados.
- Sugira metas de economia simples.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV/JSON são carregados no início da sessão do agente.
No protótipo em Python, o transacoes.csv é lido com pandas e os dados são agregados por categoria.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

- Os dados não são incluídos diretamente no system prompt.
- São consultados dinamicamente durante a interação: o agente recebe os totais por categoria e responde com base nesses valores.
- O system prompt define as regras gerais de comportamento; os dados alimentam as respostas em tempo real.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Público geral
- Limites definidos:
   - Restaurantes: R$ 350
   - Transporte: R$ 300
   - Alimentação: R$ 600

Últimas transações:
- 01/03: Supermercado Bom Preço - R$ 250 (Alimentação)
- 02/03: Uber - R$ 45 (Transporte)
- 05/03: Restaurante Sabor Caseiro - R$ 120 (Restaurantes)
- 07/03: Posto Shell - R$ 200 (Transporte)
- 15/03: Delivery Pizza - R$ 85 (Restaurantes)
- 27/03: Restaurante Gourmet - R$ 150 (Restaurantes)
```
