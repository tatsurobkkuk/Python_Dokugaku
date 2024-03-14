### Ex 1. コンピュータにある何かのファイルをPythonで開いて、コンテンツを出力しよう
import os
filename = os.path.join("/Users",
                        "tatsurotanioka",
                        "Library",
                        "Mobile Documents",
                        "com~apple~CloudDocs",
                        "Learning",
                        "scraping_python2nen",
                        "chap1",
                        "download.txt")
with open(filename, "r") as f:
    print(f.read())

### Ex 2. 何か質問するプログラムを書こう。入力された回答をファイルに書き出そう。
answer = input("How are you feeling today?")
with open("chpt9_ex2.txt", "w") as f:
     f.write(answer)

### Ex 3. リストの中身をcsvファイルに書き出そう。
import csv
with open("chpt9_ex3.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

## solution
movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

### Ex 4. チャレンジ３を日本語で同じようにやってみよう。
with open("chpt9_ex4.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(["トップガン", "卒業白書", "マイノリティー・リポート"])
    w.writerow(["タイタニック", "レヴェナント: 蘇えりし者", "インセプション"])
    w.writerow(["トレーニング デイ", "マイ・ボディガード", "フライト"])