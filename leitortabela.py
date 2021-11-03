import pandas as pd 
import numpy as np


#Limpeza de tabela comando:
#Sheet_name serve pra selecionar a aba da planilha
#usecols serve pra selecionar as colunas (começa do 0)
# Não esquecer de printar antes pra ver se ta dando certo!

df = pd.read_excel('testepib.xls', sheet_name='CEI', usecols=[0,1], header=[2])
df2 = pd.read_excel('testeipca.xlsx', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12], header=[11])
df.columns = ['Período', 'Valor']
dfanos = df.loc[{4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99,104}]
#dfanos.sort_index(ascending=True) -- Tentando organizar as index
#df.to_excel('resultadopib.xlsx') -- Converter pra tabela em xlsx
#print(dfanos)

df = df.drop([4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99,104])
#print(df) -- print do data frame
#df2.to_excel('resultadoipca.xlsx') -- Converter IPCA pra tabela em xlsx