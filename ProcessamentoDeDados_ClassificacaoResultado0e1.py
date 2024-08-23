import pandas as pd


def classify_bar(open_price, close_price):
    if open_price < close_price:
        return 1
    elif open_price > close_price:
        return 0
    else:
        return 2


def process_csv(input_file, output_file):
    # Ler o arquivo CSV de entrada
    df = pd.read_csv(input_file, sep='\t')

    # Preparar uma lista para armazenar as linhas do arquivo de saída
    output_rows = []

    # Iterar sobre o DataFrame a partir da nona linha
    for i in range(8, len(df)):
        # Obter as últimas 8 barras
        last_8_bars = df.iloc[i - 8:i]
        classifications = [classify_bar(row['<OPEN>'], row['<CLOSE>']) for index, row in last_8_bars.iterrows()]

        # Classificar a barra atual
        current_bar = df.iloc[i]
        open_price = current_bar['<OPEN>']
        close_price = current_bar['<CLOSE>']
        if abs(open_price - close_price) > 100:
            result = classify_bar(open_price, close_price)
            # Adicionar as classificações, o resultado, a data e o horário à linha de saída
            output_rows.append(classifications + [result, current_bar['<DATE>'], current_bar['<TIME>']])

    # Criar um DataFrame com os resultados
    columns = [f'barra_{j}' for j in range(1, 9)] + ['resultado', '<DATE>', '<TIME>']
    output_df = pd.DataFrame(output_rows, columns=columns)

    # Escrever o DataFrame de saída no arquivo CSV
    output_df.to_csv(output_file, index=False)


# Caminho do arquivo de entrada e de saída
input_file = 'WIN$N_M1_202309191448_202406111614.csv'
output_file = 'dados_processados_com_data_hora.csv'

# Executar a função para processar o arquivo
process_csv(input_file, output_file)
