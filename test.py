# browser_auto_foods.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome = webdriver.Chrome()

location = input("場所入力：")
favorite_foods = ["カレー", "ラーメン", "チャーハン", "とんかつ", "お好み焼き"]

for i, food in enumerate(favorite_foods):
    if i > 0:
        # 新しいタブ
        chrome.execute_script("window.open('','_blank');")
        time.sleep(5)
        chrome.switch_to.window(chrome.window_handles[i])
        time.sleep(5)
    # グーグルを開く
    chrome.get("https://www.google.com")
    time.sleep(5)

    # 検索ワード入力
    search_box = chrome.find_element_by_name("q")
    search_words = location, food
    search_box.send_keys(" ".join(search_words))

    # 検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.title)

# 先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0])