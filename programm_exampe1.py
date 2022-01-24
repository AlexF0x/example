import selenium
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import requests
import random
import xlrd
import xlsxwriter
wb = xlrd.open_workbook_xls(r'C:\Windows\System32\Untitled Folder\names.xls')
ws = wb.sheet_by_index(0)
mylist = ws.col_values(0)
row = 1
row1= 19
workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet()
for name in mylist[0:3]:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f'https://duckduckgo.com/?q={name}&t=newext&atb=v308-2__&iax=images&ia=images'
    driver.get(url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    img_link='http:'+soup.find_all('img', attrs = {'class':'tile--img__img js-lazyload'})[0]['src']
    img = requests.get(img_link)
    img_title = f'{name}.png'
    with open(img_title,'wb') as file:
        img_end=file.write(img.content)
    description=name
    worksheet.insert_image(f'B{row}', f'{img_title}', {'x_scale': 0.5, 'y_scale': 0.5})
    row+=19  
    worksheet.write(f'A{row1}', f'{description}')
    row1+=19
workbook.close()
