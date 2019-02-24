from bs4 import BeautifulSoup
import requests
import os
import urllib.request
from time import sleep


inurl=input('Input a URL')
directory=input('Enter a dir to store the image')
check=os.path.isdir(directory)
if not check:
    os.mkdir(directory)   
r=requests.get(inurl)
data=r.text
count=0
html=BeautifulSoup(data,'lxml')
img_tags=html.find_all('img')
for i in img_tags:
    
    name=i['src'].split('/')
    count=count+1
    #print(name[-1])
    urllib.request.urlretrieve(i['src'],directory+"/"+name[-1]+".jpg")
    print('Downloaded '+name[-1])
    sleep(2)
    




