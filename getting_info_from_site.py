import selenium
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
dl=soup.find_all('dd',attrs = {'class':'wp-caption-text gallery-caption small-3 columns'})
a_list=[]
for a in dl:
    a_list.append(a.find_parent('a')['href'])
master_list=[]
for link in a_list:
    data_dict={}
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f'{link}'
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    data_dict['name'] = soup.find_all('h1',attrs = {'class':'entry-title'})[0].text
    data_dict['lastfight_date'] = soup.find_all('time')[0].get_text().strip()
    data_dict['lastfight'] = soup.find_all('h4',attrs = {'class':'sp-event-title'})[0].text.strip()
    master_list.append(data_dict)
df=DataFrame(master_list)
df.to_csv('boxer_data.csv',index=False)

