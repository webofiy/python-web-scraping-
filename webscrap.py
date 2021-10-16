# simplest scrap using requstes 
import requests
from bs4 import BeautifulSoup
url ="https://www.youtube.com"
response=requests.get(url)
htm=response.content
soup=BeautifulSoup(htm,'html.parser')
dataa=soup.prettify()
print(dataa)
file=open("data.txt" ,"wb+")
file.write(dataa)
