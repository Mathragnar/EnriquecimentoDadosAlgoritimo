import pandas as pd


# Definindo a classe DataProcessor
class DataProcessor:
    # Inicializando a classe com o arquivo de saída
    def __init__(self, output_file):
        self.output_file = output_file

    # Método para contar os resultados
    def count_results(self):
        df = pd.read_csv(self.output_file)
        counts = df['resultado'].value_counts()
        percentages = counts / len(df) * 100
        return counts, percentages

    # Método para embaralhar o arquivo CSV
    def embaralhar_csv(self, arquivo_entrada, arquivo_saida):
        # Ler o arquivo CSV de entrada
        df = pd.read_csv(arquivo_entrada)

        # Embaralhar as linhas do DataFrame
        df = df.sample(frac=1).reset_index(drop=True)

        # Escrever o DataFrame embaralhado no arquivo de saída
        df.to_csv(arquivo_saida, index=False)

    # Método para excluir linhas com o valor 2
    def excluir_linhas(self, num_linhas_para_excluir):
        # Lendo o arquivo CSV
        df = pd.read_csv(self.output_file)

        # Localizando as linhas onde a coluna 'resultado' é igual a 2
        linhas_com_2 = df[df['resultado'] == 2]

        # Certificando-se de que não estamos tentando excluir mais linhas do que as disponíveis
        num_linhas_para_excluir = min(num_linhas_para_excluir, len(linhas_com_2))

        # Excluindo as linhas
        df = df.drop(linhas_com_2.index[:num_linhas_para_excluir])

        # Gerando o arquivo de saída
        df.to_csv('dados_enriquecidos_0_1_2_sem_embaralhamento.csv', index=False)

        print(f"{num_linhas_para_excluir} linhas com o valor 2 foram excluídas e o arquivo de saída foi gerado.")
