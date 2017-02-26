import requests
from bs4 import BeautifulSoup

url = "http://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
links = soup.find_all("a")

for link in links:
    #if "http" in link:
    print ("<a href='%s'>%s</a>" %(link.get("href"), link.text))
    #or > link.get("href")
    #or print link.text // print link.text, link.get("href")
    #"<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print (item.contents[0].find_all("a", {"class": "business-name"})[0].text)
    print (item.contents[1].find_all("p", {"class": "adr"})[0].text)
    try:
        print (item.contents[1].find_all("li", {"class": "primary"})[0].text)
    except:
        pass
