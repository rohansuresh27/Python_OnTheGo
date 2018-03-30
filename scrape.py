import requests
from bs4 import BeautifulSoup
#import re

# query = "https://www.inshorts.com/en/read/business"
# query = "http://www.moneycontrol.com/company-article/tataconsultancyservices/news/TCS"

query = "https://tradingeconomics.com/india/news" #URL

r = requests.get(query)
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')
x = soup.find_all('a')
#print(x)

# https://stackoverflow.com/questions/41569357/how-to-strip-all-tags-except-br-in-re-compile-python
# def cleanhtml(raw_html):
#   cleanr = re.compile('<.*?>')
#   cleantext = re.sub(cleanr, '', raw_html)
#   return cleantext


arr = []
for i in x:
	if 'style' or 'href' in str(i): # HEADLINE:'style' or'href'
		arr.append(i.text)

print (arr)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://stackoverflow.com/questions/30092474/beautiful-soup-find-get-just-the-text

# for s in soup.find_all(id="rhs_block"):
#    print(s.text)

# print(soup.prettify())
