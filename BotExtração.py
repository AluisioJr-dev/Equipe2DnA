#selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd 
import numpy as np
import os.path
import os


#misc
import datetime
from time import gmtime, strftime
from zipfile import ZipFile
from datetime import date
import re, time, os, errno, codecs, sys

#Pathlib
import pathlib as pl

wait_time = 3
    # Define as funcoes utilizadas no script.
def left(s, amount):
        return s[:amount]

def right(s, amount):
        return s[-amount:]

def mid(s, offset, amount):
        return s[offset:offset+amount]

def check_if_path_exists(path):
        if os.path.exists(path) == False:
               os.makedirs(path)

def simplecount(filename):
        lines = 0
        for line in open(filename):
            lines += 1
        return lines
#numpy #matplotlib

"""
driver = webdriver.Chrome()

driver.get('https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=US')

time.sleep(wait_time)
elem_data = driver.find_element_by_css_selector("#hf_footer_wrapper > div.privacy-widget > button")
elem_data.click()
elem_data = driver.find_element_by_link_text('EXCEL')
elem_data.click()
time.sleep(wait_time)
driver.get('https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=downloads&utm_source=landing&utm_medium=explica&utm_campaign=pib#evolucao-taxa')

time.sleep(wait_time)

elem_data = driver.find_element_by_id("Contas_Nacionais/Contas_Nacionais_Trimestrais/Tabelas_Completas_anchor")
elem_data.click()

elem_data = driver.find_element_by_id("j1_65_anchor")
elem_data.click()

driver.get('https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html?=&t=series-historicas#')

time.sleep(wait_time)

elem_data = driver.find_element_by_id("tabelasidra20171059636838export")
elem_data.click()

elem_data = driver.find_element_by_xpath("//option[@value='xls']")
elem_data.click()
time.sleep(wait_time)

driver.get('https://data.bls.gov/timeseries/CUSR0000SA0&output_view=pct_1mth')
#COLETAR DADOS DE 2001 ATÉ 2020

time.sleep(wait_time)

elem_data = driver.find_element_by_id("download_xlsx0")
elem_data.click()
time.sleep(wait_time)


driver.quit()
"""
zipa = ZipFile("C:/Users/RR854YA/Downloads/Tab_Compl_CNT.zip", 'r')
zipa.ZipFile.extract(path=None, member="Tab_Compl_CNT.zip", pwd=None)
"""
#Limpeza de tabela comando:
#Sheet_name serve pra selecionar a aba da planilha
#usecols serve pra selecionar as colunas (começa do 0)
# Não esquecer de printar antes pra ver se ta dando certo!

#COMEÇO DATA FRAME GDP
df = pd.read_excel('C:/Users/RR854YA/Downloads/testepibusa.xls', sheet_name='Data') 
df = df[df.columns[[-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8,-7,-6,-5,-4,-3, -2, -1]]]
anoatual= datetime.datetime.now()

df.columns=[anoatual.year-20, anoatual.year-19, anoatual.year-18, anoatual.year-17, anoatual.year-16, anoatual.year-15, anoatual.year-14, anoatual.year-13, anoatual.year-12, anoatual.year-11, anoatual.year-10, anoatual.year-9, anoatual.year-8, anoatual.year-7, anoatual.year-6, anoatual.year-5, anoatual.year-4, anoatual.year-3, anoatual.year-2, anoatual.year-1]

df = df.loc[[254]]


df2 = pd.DataFrame(data=df)
dfGDP = df2.T
dfGDP.columns=['Valor em Trilhão de US$']
dfGDP['Valor em Trilhão de US$'] = dfGDP['Valor em Trilhão de US$'].astype(np.int64)
dfGDP['Valor em Trilhão de US$'] = (dfGDP['Valor em Trilhão de US$']/1000000).apply(lambda x: '{:,.2f}'.format(x))
dfGDP = dfGDP.reset_index()
dfGDP.columns=['Período', 'PIB USA - Valor em Trilhão de US$']
#print(dfGDP)

#FIM DATA FRAME GDP
#INICIO DATA FRAME PIB
dfpib = pd.read_excel('C:/Users/RR854YA/Downloads/testepib.xls', sheet_name='CEI', usecols=[0,1]) 
#print(dfpib)
dfpib.columns = ['Período', 'PIB BRASIL - Valor em Trilhão de R$']
dfpib = dfpib.drop([0, 1,109])
dfpib['PIB BRASIL - Valor em Trilhão de R$'] = dfpib['PIB BRASIL - Valor em Trilhão de R$'].astype(np.int64)

dfpib['PIB BRASIL - Valor em Trilhão de R$'] = (dfpib['PIB BRASIL - Valor em Trilhão de R$']).apply(lambda x: '{:,.2f}'.format(x))
dfpib = dfpib[~dfpib.Período.str.contains("I", na=False)]
dfpib = dfpib.tail(20)
#print(dfpib)
dfpibb = dfpib.merge(dfGDP, left_on="Período", right_on="Período")
#print(dfpibb)

#dfpibb.to_excel('resultadopib33.xls')
#FIM DATA FRAME PIB

#COMEÇO DATA FRAME IPCA
dfipca = pd.read_excel('C:/Users/RR854YA/Downloads/20211104163039.xlsx', usecols=[0,1, 2]) 
dfipca.columns=["Período", "delete", "BRA - Variação Acumulada em %"]
dfipca = dfipca.drop([0, 1, 29, 28])
dfipca.drop('delete', inplace=True, axis=1)
dfipca['Período'] = dfipca['Período'].apply(lambda x: x.split(' ')[-1])
dfipca = dfipca.tail(20)


#print(dfipca)
#FIM DATA FRAME IPCA
#INICIO DATA FRAME CPI

dfCPI = pd.read_excel('C:/Users/RR854YA/Downloads/SeriesReport-20211104162928_69ae79.xlsx', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12], header=[11]) 

dfCPI["Variação Acumulada em %"] = dfCPI.drop('Year', axis=1).sum(axis=1)
dfCPI = dfCPI.drop(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], axis=1)
dfCPI.columns=["Período", "USA - Variação Acumulada em %"]
dfCPI['Período'] = dfCPI['Período'].astype(np.str0)

dfCPI['Período'] = dfCPI['Período'].apply(lambda x: x.split('.0')[0])
dfCPI = dfCPI.tail(20)
dfCPI['USA - Variação Acumulada em %'] = (dfCPI['USA - Variação Acumulada em %']).apply(lambda x: '{:,.2f}'.format(x))
#FIM DATA FRAME CPI

dfipcaU = dfipca.merge(dfCPI, left_on="Período", right_on="Período")
"""
print(dfipcaU)