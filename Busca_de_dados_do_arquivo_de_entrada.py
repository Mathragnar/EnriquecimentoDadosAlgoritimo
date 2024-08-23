import pandas as pd

# Lendo o arquivo xlsx
df = pd.read_excel('Teste.xlsx')

# Iterando sobre as colunas
for col in df.columns:
    # Selecionando apenas os dados não-NaN
    non_nan_data = df[col].dropna()

    # Imprimindo a coluna e seus dados não-NaN
    print(f'\nColuna: {col}')
    print(non_nan_data)

# Selecionando apenas os dados não-NaN da coluna 'Unnamed: 4'
non_nan_data = df['Unnamed: 4'].dropna()

# Imprimindo a coluna e seus dados não-NaN
print('\nColuna: Unnamed: 4')
print(non_nan_data.to_string(index=False))

# Buscando os dados entre as linhas 'Volume'
start = df[df['Unnamed: 4'] == 'Volume'].index[0]
end = df[df['Unnamed: 4'] == 'Volume'].index[1]
data = df.loc[start+1:end-1, 'Unnamed: 4']

# Selecionando apenas os dados não-NaN
non_nan_data = data.dropna()

# Imprimindo a coluna e seus dados não-NaN
print('\nColuna: Unnamed: 4 (entre as linhas \'Volume\')')
print(non_nan_data.to_string(index=False))
