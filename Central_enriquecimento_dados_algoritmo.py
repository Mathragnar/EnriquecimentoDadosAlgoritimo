# Importando as classes necessárias
from ProcessamentoDeDados_ClassificacaoResultado0_1_2 import BarClassifier
from DadosPorcentagemContagemEmbaralhamento import DataProcessor


def main():
    # Definindo os arquivos de entrada e saída
    input_file = 'WIN@N_M1_202310200904_202407101017.csv'
    output_file = 'dados_processados_com_data_hora_resultado_0_1_2.csv'

    # Criando uma instância da classe BarClassifier
    classifier = BarClassifier(input_file, output_file)

    # Processando o arquivo CSV usando a classe BarClassifier
    classifier.process_csv()

    # Criando uma instância da classe DataProcessor com o arquivo de saída
    processor = DataProcessor(output_file)

    # Contando os resultados usando a classe DataProcessor
    counts, percentages = processor.count_results()

    # Imprimindo os resultados
    for value in counts.index:
        print(f"Valor: {value}, Contagem: {counts[value]}, Porcentagem: {percentages[value]:.2f}%")

    # Perguntando ao usuário quantas linhas com o valor 2 devem ser excluídas
    num_linhas_para_excluir = int(input("Quantas linhas com o valor 2 você deseja excluir? "))

    # Excluindo linhas com o valor 2 usando a classe DataProcessor
    processor.excluir_linhas(num_linhas_para_excluir)

    # Embaralhando o arquivo de saída usando a classe DataProcessor
    processor.embaralhar_csv('dados_enriquecidos_0_1_2_sem_embaralhamento.csv',
                             'dados_enriquecidos_0_1_2_embaralhado.csv')


# Verificando se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
