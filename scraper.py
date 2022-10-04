import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
 
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#print(soup)

results = soup.find(id="ResultsContainer")

titles = []
titles_html = results.find_all("h2",class_="title")
#print(titles_html)

for title in titles_html:
    titles.append(title.text.strip())

for i in range(len(titles)):
    print(titles[i])
