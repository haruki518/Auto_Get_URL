import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.jp/search'

req = requests.get(url, params={'q': 'python'})
python_URL = requests.get(req.url)

soup = BeautifulSoup(python_URL.text, "html.parser")

for i in range(5):
    for a in soup.select('.g > a'):
        U = a.get('href').replace('/url?q=','')
        with open("T.csv","a")as f:
            f.write(U)