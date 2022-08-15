from bs4 import BeautifulSoup

import requests


editoriaKogut = ("/noticias-da-tv/novelas/noticia")

html1 = requests.get("https://kogut.oglobo.globo.com/noticias-da-tv/novelas/ultimas-noticias.html").content
html2 = requests.get("https://kogut.oglobo.globo.com/noticias-da-tv/novelas/ultimas-noticias/2.html").content
html3 = requests.get("https://kogut.oglobo.globo.com/noticias-da-tv/novelas/ultimas-noticias/3.html").content

soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')
soup3 = BeautifulSoup(html3, 'html.parser')

listOfUrls = []

for a in soup1.find_all('a', class_="more", href=True):
    if(editoriaKogut) in a['href']:
      listOfUrls.append(a['href'])

for a in soup2.find_all('a', class_="more", href=True):
    if(editoriaKogut) in a['href']:
      listOfUrls.append(a['href'])

for a in soup3.find_all('a', class_="more", href=True):
    if(editoriaKogut) in a['href']:
      listOfUrls.append(a['href'])

filtredList  = set(listOfUrls)



for url in filtredList:
  html = requests.get("https://kogut.oglobo.globo.com" + url).content

  soup = BeautifulSoup(html, 'html.parser')
  
  ids = soup.find_all('script')
  selectID = []
  for id in ids:
     if ("tea_materia_id = ") in str(id):
       selectID.append(id)

  id = str(selectID[1]).split()[3]   
  print(id)