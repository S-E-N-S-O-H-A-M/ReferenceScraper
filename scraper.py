from bs4 import BeautifulSoup
import csv
import time
import requests

url='https://en.wikipedia.org/wiki/Real_Madrid_CF'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'} # google my user agent


txt_file=open("reference.txt",'w')


html_page=requests.get(url,headers=headers)
soup=BeautifulSoup(html_page.content,'lxml')
info_one=soup.find_all("div",{'class':"reflist",'style':"list-style-type: decimal;"})[1].find("ol")

for i in range(0,10):
        info_two=info_one.find_all("li")[i].get_text()
        txt_file.write("\n")
        txt_file.write(info_two)
txt_file.close()


