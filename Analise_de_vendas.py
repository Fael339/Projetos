import pandas as pd

#Leitura dos dados
df = pd.read_csv('vendas.csv')

#Exibe a tabela no terminal
print(df)

#Total de vendas por loja
df['Valor_Total'] = df['Quantidade'] * df["Preco_Unitario"] * (1 - df['Desconto (%)']/100)
vendas_por_loja = df.groupby('Loja')['Valor_Total'].sum()

#Exibir vendas por loja
print (vendas_por_loja)

#Agrupa vendas por vendedor
vendas_por_vendedor = df.groupby('Vendedor')['Valor_Total'].sum()

#Exibir vendas por vendedor
print(vendas_por_vendedor)

#Agrupar por produto e somar quantidade vendida
produtos_mais_vendidos =df.groupby('Produto')['Quantidade'].sum()

#Ordenar do maior para o menor
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(ascending=False)

#Exibir produtos mais vendidos
print(produtos_mais_vendidos)