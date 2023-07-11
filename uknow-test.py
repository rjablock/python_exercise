import requests
from bs4 import BeautifulSoup
import time

for i in range(1, 6):
    # WebページのURL
    url = "https://eikaiwa.dmm.com/uknow/questions/" + str(i)

    # requestsを使ってWebページを取得
    response = requests.get(url)

    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # 解析したHTMLからIDが"question-title"の部分を取り出す
        question_title = soup.find(id="question-title")
  
        # 結果をファイルに追記
        with open("uknow-test.txt", "a") as file:
            file.write(str(i) + ". " + question_title.get_text() + "\n")
    except AttributeError:
        pass

    # 次のリクエストまでの待機時間（秒）
    time.sleep(1)