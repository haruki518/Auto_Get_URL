import requests
from bs4 import BeautifulSoup

with open('keys.csv', encoding='UTF-8') as csv_file:
    with open('result.csv','w',encoding='UTF-8') as f:

        for keys in csv_file:
            result = requests.get('https://www.google.com/search?q={}/'.format(keys))
            soup = BeautifulSoup(result.text, 'html.parser')
            list = soup.findAll(True, {'class' : 'BNeawe vvjwJb AP7Wnd'})

            for i in range(3):
                a = str(list[i]).strip('<div class="BNeawe vvjwJb AP7Wnd">')
                result_title = a.strip('</')
                keyword = keys.rstrip("\n")
                f.write('{0},{1}\n'.format(keyword, result_title))


#target divs example
    # <div class="BNeawe vvjwJb AP7Wnd">フィリピン人女性5つの特徴
    # <div class="BNeawe vvjwJb AP7Wnd">フィリピン人 - Wikipedia


