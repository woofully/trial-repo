import urllib.request as urr
import bs4

sauce = urr.urlopen('https://www.saasmag.com/saas-1000-2019/2').read()
soup = bs4.BeautifulSoup(sauce,'html.parser')

table = soup.find("table")

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)