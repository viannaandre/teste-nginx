#Definição de bibliotecas
#Base a ser utilizada POSTGRESQL
#DASHBOARD GRAPHANA
#APP PYTHON para WEBCrawler
#import psycopg2
import requests
import base64
#from selenium import webdriver
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
#from requests.auth import HTTPBasicAuth
import time

#Criando a logica para Scrapping
modem0 = "http://192.168.15.1/login.asp"
#modem1="http://192.168.15.1/settings-local-network.asp"
senha = ['lixo', 'lixo']
userpass = senha[0] + ':' + senha[1]
encoded_u = base64.b64encode(userpass.encode()).decode()
id_secret_bytes = bytes(userpass, "UTF-8")
token = base64.b64encode(id_secret_bytes)
#print (encoded_u)
#print (token)

page = requests.get(modem0)
#Valida status HTTP 200=OK
print(page.status_code)
#browser = webdriver.Chrome()
#browser.get (modem0)
#time.sleep(3)
#USER = senha[0]
#PASS = senha[1]

user = browser.find_element('name', 'Usuário')
passw = browser.find_element('name', 'Senha')
user.send_keys(USER)
passw.send_keys(PASS)

time.sleep(2)
login_attempt = browser.find_element_by_id('ENTRAR').click()
time.sleep(5)

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
lista = soup.find_all('html')

print(lista)

#headers = {"Authorization": "Basic %s" %encoded_u}
#r = requests.get(modem0, auth=HTTPBasicAuth(senha[0], senha[1]))
#print(r.status_code)
#print(r.request.headers['Authorization'])
#print(r.request.headers)
#header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
#          "Authorization": r.request.headers['Authorization']
#          }
#print(headers)
#print(r.text)

#PARSE HTML
#r = requests.get(modem1, headers=header, data={})
#res = r.text
#print(res)
#soup = BeautifulSoup(r.text, 'html.parser')

#main_title_element = soup.find(id='main-title')
#print(main_title_element)
#quote_elements = soup.find_all('div')
#print(quote_elements)