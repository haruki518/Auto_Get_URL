import time                                 # スリープを使うために必要
from selenium import webdriver              # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary                  # パスを通すためのコード

driver = webdriver.Chrome()                 # Chromeを準備

# サンプルのHTMLを開く
driver.get('https://www.google.com/')       # Googleを開く

search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
search.send_keys('WATLABブログ')             # 検索ワードを送信する
search.submit()                             # 検索を実行
time.sleep(3)                               # 3秒間待機
def ranking(driver):
    i = 1               # ループ番号、ページ番号を定義
    i_max = 2           # 最大何ページまで分析するかを定義
    title_list = []     # タイトルを格納する空リストを用意
    link_list = []      # URLを格納する空リストを用意
    
    # 現在のページが指定した最大分析ページを超えるまでループする
    while i <= i_max:
        # タイトルとリンクはclass="r"に入っている
        class_group = driver.find_elements_by_class_name('r')
        # タイトルとリンクを抽出しリストに追加するforループ
        for elem in class_group:
            title_list.append(elem.find_element_by_class_name('LC20lb').text)           #タイトル(class="LC20lb")
            link_list.append(elem.find_element_by_tag_name('a').get_attribute('href'))  #リンク(aタグのhref属性)
 
        # 「次へ」は1つしかないが、あえてelementsで複数検索。空のリストであれば最終ページの意味になる。
        if driver.find_elements_by_id('pnnext') == []:
            i = i_max + 1
        else:
            # 次ページのURLはid="pnnext"のhref属性
            next_page = driver.find_element_by_id('pnnext').get_attribute('href')
            driver.get(next_page)   # 次ページへ遷移する
            i = i + 1               # iを更新
            time.sleep(3)           # 3秒間待機
    return title_list, link_list    # タイトルとリンクのリストを戻り値に指定