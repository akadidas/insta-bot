import requests
from bs4 import BeautifulSoup
from urllib import request
import cfscrape


usr=(input("enter your user id here"))
ur="https://www.instagram.com/"+usr+"/"
print(ur)


scraper = cfscrape.create_scraper()

source_code=str(scraper.get(ur).content)


        
soup=BeautifulSoup(source_code,"html.parser")
print(soup)
for link in soup.findAll('meta',property='og:image'):


    src=link.get('content')

print(src)
address=src.split('s150x150')
url=address[0]+'s640x640'+address[1]
print("url is",url)



def download_csv(url):

    response=request.urlopen(url)
    csv=response.read();
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=r'prof.jpeg'
    fx=open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_csv(url)
