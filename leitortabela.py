import pandas as pd 
import numpy as np


#Limpeza de tabela comando:
#Sheet_name serve pra selecionar a aba da planilha
#usecols serve pra selecionar as colunas (começa do 0)
# Não esquecer de printar antes pra ver se ta dando certo!
tabela = pd.read_excel('C:/Users/RR854YA/Downloads/testepib.xls', sheet_name='CEI', usecols=[0,1])


tabela.columns = ['Período', 'Valor em Trilhão de R$']
tabela = tabela.drop([0, 1,109])
tabela['Valor em Trilhão de R$'] = tabela['Valor em Trilhão de R$'].astype(np.int64)




tabela['Valor em Trilhão de R$'] = (tabela['Valor em Trilhão de R$']/1000000).apply(lambda x: '{:,.2f}'.format(x))
#tabela
print(tabela)

#tabela.to_excel('resultadopib2.xls')