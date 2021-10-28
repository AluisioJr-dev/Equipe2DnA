#selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#misc
import datetime
from time import gmtime, strftime
from datetime import date
import re, time, os, errno, codecs, sys

#Pathlib
import pathlib as pl

wait_time = 5

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
driver.quit()
