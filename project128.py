from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import requests
import pandas as pd


start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(start_url)
soup=BeautifulSoup(page.text, 'html.parser')
browser=webdriver.Chrome("D:\chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["Proper name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)"]
    star_data=[]
    star_table=soup.find_all('table')
    table_rows=star_table[7].find_all('tr')
    
    
    for tr_tag in soup.find_all("tr"):
        td_tags=tr_tag.find_all("td")
        temp_list=[]

        for index, td_tag in enumerate(td_tags):

            if index == 0:
                temp_list.append(td_tag.contents[0])
            else:
                temp_list.append("")   
        star_data.append(temp_list)

    for td_tag in star_data:
        row = [i.text.rstrip() for i in td_tag]

    name=[]
    radius=[]
    mass=[]
    distance=[] 
       

    for star_data in star_table:
        name.append(star_data[0])
        radius.append(star_data[9])
        mass.append(star_data[8])
        distance.append(star_data[5])

    d = {'name', 'radius', 'mass', 'distance'}
    df = pd.DataFrame(data=d)
    
  
    with open("new.csv", "w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)  


scrape()
