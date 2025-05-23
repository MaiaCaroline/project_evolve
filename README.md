# 📊 Dashboard de Customer Success

Um dashboard interativo desenvolvido em Streamlit para análise de métricas de Customer Success, retenção de clientes e identificação de oportunidades de negócio.

##  Deploy no Streamlit Cloud

Este dashboard está pronto para deploy no Streamlit Cloud. Siga os passos:

1. **Fork este repositório** no seu GitHub
2. **Acesse [share.streamlit.io](https://share.streamlit.io)**
3. **Conecte sua conta GitHub**
4. **Selecione este repositório**
5. **Configure:**
   - **Main file path:** `dashboard_cliente_success.py`
   - **Python version:** 3.9
6. **Deploy!** 🎉

## 🎯 Funcionalidades

- **📈 Métricas de Retenção:** Taxa de churn, NPS médio, ticket médio
- **🎯 Segmentação de Clientes:** Clustering automático por comportamento
- **🚨 Alertas de Churn:** Identificação de clientes em risco
- **💰 Oportunidades de Upsell:** Clientes com potencial de crescimento
- **📊 Visualizações Interativas:** Gráficos dinâmicos e filtros
- **📁 Upload de Dados:** Suporte para dados customizados via CSV

## 🗂️ Estrutura de Dados

O dashboard aceita arquivos CSV com as seguintes colunas (opcionais):

| Coluna | Descrição | Alternativas aceitas |
|--------|-----------|---------------------|
| `cliente_id` | Identificador único do cliente | `CD_CLIENTE`, `CLIENTE`, `CD_CLI` |
| `VL_TOTAL_CONTRATO` | Valor do contrato | `VALOR_CONTRATO`, `VL_CONTRATO` |
| `resposta_NPS_x` | Nota NPS (0-10) | `NPS`, `NOTA_NPS` |
| `SITUACAO_CONTRATO` | Status do contrato | `STATUS_CONTRATO`, `SITUACAO` |
| `DT_ASSINATURA_CONTRATO` | Data de assinatura | `DATA_ASSINATURA`, `DT_CONTRATO` |
| `DS_SEGMENTO` | Segmento de mercado | - |
| `UF` | Estado/região | - |

## 💻 Instalação Local

```bash
# Clone o repositório
git clone <seu-repositorio>
cd dashboard-customer-success

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run dashboard_cliente_success.py
```

## 📝 Como Usar

### 1. **Dados de Exemplo**
- O dashboard funciona automaticamente com dados de exemplo
- Perfeito para demonstrações e testes

### 2. **Upload de Dados Personalizados**
- Use o painel lateral para fazer upload do seu arquivo CSV
- O sistema detecta automaticamente as colunas compatíveis
- Suporta até 5000 registros para performance otimizada

### 3. **Filtros e Análises**
- Filtre por cluster de clientes
- Visualize métricas em tempo real
- Identifique oportunidades e riscos

## 🔧 Configuração

### Clusters de Clientes
O sistema classifica automaticamente os clientes em:

- **🟢 Regular:** Clientes com comportamento padrão
- **🔴 Risco de Churn:** NPS ≤ 5 ou critérios de risco
- **🟡 Potencial de Upsell:** NPS ≥ 8 e valor abaixo da mediana

### Métricas Calculadas
- **Taxa de Churn:** Baseada em contratos com mais de 12 meses
- **NPS Score:** (% Promotores - % Detratores)
- **Ticket Médio:** Valor médio dos contratos por cluster

## 🌐 Exemplo de Deploy

Veja o dashboard em funcionamento: [Link do seu deploy aqui]

## 🛠️ Tecnologias

- **Streamlit:** Framework web para Python
- **Pandas:** Manipulação de dados
- **Plotly:** Visualizações interativas
- **NumPy:** Computação numérica

## 📞 Suporte

Para dúvidas ou sugestões:
- Abra uma issue no GitHub
- Contribuições são bem-vindas!

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido para análise de Customer Success** 📊 