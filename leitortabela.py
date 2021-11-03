import pandas as pd 
import numpy as np


#Limpeza de tabela comando:
#Sheet_name serve pra selecionar a aba da planilha
#usecols serve pra selecionar as colunas (começa do 0)
# Não esquecer de printar antes pra ver se ta dando certo!
tabela = pd.read_excel('testepib.xls', sheet_name='CEI', usecols=[0,1])
print(tabela)

"tabela.to_excel('resultadopib.xls')"