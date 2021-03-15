import requests
from bs4 import BeautifulSoup
import os

def get_html(url):
    result = requests.get(url)
    return result.text

def get_url(html):
    soup = BeautifulSoup(html, 'lxml')
    book = soup.find("p").find_all("a")
    for item in book:
        url_book.append(item.get("href"))

url_book = []
html = get_html("https://sheba.spb.ru/shkola/mat.htm")
get_url(html)

def get_url_pdf(adr):
	for url in adr:
		try:
			link_book = ("https://sheba.spb.ru/shkola/" + url)
			html_book = requests.get(link_book).text

			bs = BeautifulSoup(html_book, 'lxml')
			link = bs.find("p").find("a").get("href")
			name = bs.find("h1").text
			
			pdf_url.append({name: link})
			#print(type(link), link)
		except:
			print("Книга удалена ", name)

pdf_url = []

get_url_pdf(url_book)

def download(pdf):
	for item in pdf:
		try:	
			for i in item.items():
				kek = requests.get("https://sheba.spb.ru/shkola/" + str(i[1]))
				f = open(str(i[0]) , "wb")
				f.write(kek.content)
		except:
			for i in item.items():
				kek = requests.get("https://sheba.spb.ru" + str(i[1]))
				f = open(str(i[0]) , "wb")
				f.write(kek.content)
	f.close()


download(pdf_url)