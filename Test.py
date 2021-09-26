
'''Temperature in bangkok'''
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

''' 1 - URL '''
url = 'https://www.tmd.go.th/province.php?id=37'

''' 2 - Request URL '''
webopen = req(url)
page_html = webopen.read()
webopen.close()

''' 3 - Convert page_html to soup  Object '''
data = soup(page_html, 'html.parser')

''' 4 - Find Element ( td : 'strokeme' )'''
temp = data.findAll('td',{'class':'strokeme'})
province = data.findAll('span',{'class':'title'})
pv = province[0].text.replace(' ','')

result = temp[0].text
print(f'จังหวัด :{pv} อุณหภูมิ : {result}')

