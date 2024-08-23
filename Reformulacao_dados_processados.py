import pandas as pd

# Carrega o arquivo 'dados_processados_com_data_hora.csv'
dados_processados = pd.read_csv('dados_processados_com_data_hora.csv')

# Remove as colunas 'resultado', '<DATE>' e '<TIME>'
dados_processados = dados_processados.drop(['resultado', '<DATE>', '<TIME>'], axis=1)

# Salva o DataFrame resultante no arquivo 'dados_processados.csv'
dados_processados.to_csv('dados_processados.csv', index=False)
