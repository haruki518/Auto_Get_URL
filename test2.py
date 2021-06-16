from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary  
import time                # パスを通すためのコード


def target_search():
    target = ("Cisco","Python","VXLAN")
    for i in target:
        driver = webdriver.Chrome()                 # Chromeを準備
        driver.get('https://www.google.com/')       # Googleを開く
        search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
        search.send_keys(i)             # 検索ワードを送信する
        search.submit()                             # 検索を実行
        time.sleep(2)                               # 5秒間待機
        driver.quit()

target_search()        
                               # ブラウザを閉じる