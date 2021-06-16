from urllib import request

response = request.urlopen('https://www.pasonatech.co.jp/')
content = response.read()
response.close()
html = content.decode()

title = html.split('<title>')[1].split('</title')[0]
print(title)