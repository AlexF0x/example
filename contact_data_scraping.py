import selenium
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://avena.io/nutriologo/list'
driver.get(url)
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
links=soup.find_all('a', attrs = {'class':'btn_listing'})
link_list=[]
for x in links:
    link_list.append(x['href'])
new_link=[]
for item in link_list:
    if item not in new_link:
        new_link.append(item)
master_list=[]
for link in new_link:
    data_dict={}
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f'https://avena.io/nutriologo/{link}'
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    name=soup.find_all('div', attrs = {'class':'col-lg-8 col-md-12'})[0]
    data_dict['Name']=name.find_all('h1')[0].text
    soc=soup.find_all('div', attrs = {'class':'col-12'})[0]
    import re
    wh=soup.find_all(href=re.compile('wa.me'))
    whatsaap=[]
    for x in wh:
        whatsaap.append(x['href'])
    if len(whatsaap)==0:
        whatsaap.append('none')
    inst=soup.find_all(href=re.compile('www.instagram.com'))
    instagram=[]
    for x in inst:
        instagram.append(x['href'])
    if len(instagram)==0:
        instagram.append('none')
    data_dict['whatsapp']=whatsaap
    data_dict['instagram']=instagram
    master_list.append(data_dict)
df=DataFrame(master_list)
df.to_excel('nutriologo.xlsx')