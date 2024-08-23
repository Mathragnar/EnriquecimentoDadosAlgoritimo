import pandas as pd


def classify_bar(open_price, close_price):
    if open_price < close_price:
        return 1
    elif open_price > close_price:
        return 0
    else:
        return 2


class BarClassifier:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process_csv(self):
        # Ler o arquivo CSV de entrada
        df = pd.read_csv(self.input_file, sep='\t')

        # Preparar uma lista para armazenar as linhas do arquivo de saída
        output_rows = []

        # Iterar sobre o DataFrame a partir da nona linha
        for i in range(8, len(df)):
            # Obter as últimas 8 barras
            last_8_bars = df.iloc[i - 8:i]
            classifications = [classify_bar(row['<OPEN>'], row['<CLOSE>']) for index, row in
                               last_8_bars.iterrows()]

            # Classificar a barra atual
            current_bar = df.iloc[i]
            open_price = current_bar['<OPEN>']
            close_price = current_bar['<CLOSE>']
            if abs(open_price - close_price) > 100:
                result = classify_bar(open_price, close_price)
                # Adicionar as classificações, o resultado, a data e o horário à linha de saída
                output_rows.append(classifications + [result, current_bar['<DATE>'], current_bar['<TIME>']])

        # Criar um DataFrame com os resultados
        columns = ['barra_1', 'barra_2', 'barra_3', 'barra_4', 'barra_5', 'barra_6', 'barra_7', 'barra_8', 'resultado',
                   '<DATE>', '<TIME>']
        output_df = pd.DataFrame(output_rows, columns=columns)

        # Escrever o DataFrame de saída no arquivo CSV
        output_df.to_csv(self.output_file, index=False)
