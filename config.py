"""
Configurações do Dashboard de Customer Success
"""

# Configurações de dados
MAX_ROWS = 5000
RANDOM_SEED = 42

# Mapeamento de colunas
COLUMN_MAPPING = {
    'cliente': ['cliente_id', 'CD_CLIENTE', 'CLIENTE', 'CD_CLI'],
    'valor': ['VL_TOTAL_CONTRATO', 'VALOR_CONTRATO', 'VL_CONTRATO'],
    'data': ['DT_ASSINATURA_CONTRATO', 'DATA_ASSINATURA', 'DT_CONTRATO'],
    'status': ['SITUACAO_CONTRATO', 'STATUS_CONTRATO', 'SITUACAO'],
    'nps': ['resposta_NPS_x', 'NPS', 'NOTA_NPS']
}

# Status de contratos ativos
STATUS_ATIVOS = ['ATIVO', 'VIGENTE', 'ATIVA', 'REGULAR']

# Critérios de segmentação
CRITERIOS_CHURN = {
    'nps_baixo': 5,
    'nps_critico': 7,
    'dias_antigo': 730
}

CRITERIOS_UPSELL = {
    'nps_alto': 8,
    'percentil_valor': 0.5
}

# Cores do tema
CORES = {
    'primary': '#2E86C1',
    'success': '#27AE60',
    'warning': '#F39C12',
    'danger': '#E74C3C',
    'info': '#3498DB',
    'light': '#F8F9FA',
    'dark': '#2C3E50'
}

# Configurações de gráficos
COLORS_CLUSTER = {
    'Regular': CORES['info'],
    'Risco de Churn': CORES['danger'],
    'Potencial de Upsell': CORES['success']
}

COLORS_NPS = {
    'Detrator': CORES['danger'],
    'Neutro': CORES['warning'],
    'Promotor': CORES['success']
}

# Configurações de demo
DEMO_CONFIG = {
    'n_clientes': 1000,
    'segmentos': ['MANUFATURA', 'SERVIÇOS', 'VAREJO', 'FINANCEIRO', 'TECNOLOGIA'],
    'ufs': ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'GO', 'PE'],
    'probabilidades_uf': [0.3, 0.15, 0.12, 0.08, 0.08, 0.06, 0.06, 0.08, 0.07],
    'probabilidades_nps': [0.02, 0.03, 0.05, 0.08, 0.12, 0.15, 0.20, 0.15, 0.10, 0.07, 0.03],
    'probabilidades_status': [0.7, 0.2, 0.08, 0.02]
}

# Mensagens do sistema
MENSAGENS = {
    'upload_sucesso': '✅ Arquivo carregado com sucesso!',
    'erro_upload': '❌ Erro ao ler o arquivo: {}',
    'dados_exemplo': '📄 Usando dados de exemplo para demonstração',
    'sem_dados': '❌ Não foi possível carregar os dados',
    'dados_filtrados': '📊 Dados filtrados: {} registros',
    'total_registros': '📊 Total de registros: {}',
    'sem_churn': '✅ Nenhum cliente em risco de churn na seleção atual!',
    'sem_upsell': 'ℹ️ Nenhuma oportunidade de upsell na seleção atual.'
}

# Configurações de formatação
FORMATO_MOEDA = 'R$ {:,.0f}'
FORMATO_NUMERO = '{:,}'
FORMATO_PERCENTUAL = '{:.1f}%' 