# Challenge 1: 好きなミュージシャンのリストを作ろう
my_list = list()
my_list = ["Clairo",
           "Holly Humberstone",
           "Japanese House",
           "Ashe",
           "Iris"]
print("My favourite musicians:", my_list)

# Challenge 2: タプルのリストを作ろう。各タプルにはあなたが行ったことのある場所の緯度と経度を持たせよう。
my_tuple = list()
my_tuple = [(40.416775, -3.703790),
            (35.73920, 140.10502000),
            (46.392410, -94.636230),
            (33.669445, -117.823059),
            (35.646572, 139.653244)
            ]
print("Latitude-Longitude of places I lived in", my_tuple)

# Challenge 3: 辞書を作ろう。辞書にはあなたの特徴を表すキーバリューのペアを持たせよう。
# たとえば、身長、好きな色、好きな作家など
my_dict = dict()
my_dict = {
    "身長": 163,
    "生年月日": ("1991.04.03", "牡羊座"),
    "血液型": "O型",
    "仕事": "再保険",
    "趣味": "読書",
    "特技": "研究",
    "好きな食べ物": "カレー",
    "嫌いな食べ物": "にんじん"
}
print("My personal dictionary", my_dict)

# Challenge 4: 任意のキーを入力させるプログラムを書こう。入力されたキーを使って、
# １つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。
key = input("キーを入力してください：")
if key in my_dict:
    attribute = my_dict[key]
    print(attribute)
else:
    print("見つかりません。")

# Challege 5: あなたが好きなミュージシャンを辞書のキーに入れて、そのバリューとしてそのミュージシャンの
# 曲をリストで持たせよう。
my_musicians = dict()
my_musicians = {
    "Clairo": ["Sofia",
               "Alewife",
               "Impossible"],
    "Holly Humberstone": ["Antichrist",
                          "Can You Afford to Lose Me?",
                          "Overkill"],
    "The Japanese House": ["Dionne",
                           "Something Has to Change",
                           "Maybe You're the Reason"]
}
print("My favorite musicians and their songs", my_musicians)

# Challenge 6: Pythonの組み込みコンテナ型の１つにsetがあるがこれは何に使われるのだろうか？
# Set（集合型）は、集合を扱うデータ型で、リストと非常に似ているが、特徴として、重複した値を格納できない点や、
# 添字やキーなどの概念がなく、ユニークな要素である点、要素の順序を保持しない点などの特徴がある。
# この特徴を生かし、セット型では、集合、積集合、差集合などの集合演算を行ったり、データの
# 種類を管理するのに適している。
# see https://www.sejuku.net/blog/21923

# example
s = {10, 20, 30, 40, 50, 50}
print(type(s))   # 重複する値は取り除かれるため、一意な値のみが要素として残る
print(s)
s.add(100)       # set型オブジェクトに要素を追加するには、addメソッドを使います。
# print(s)
s.remove(10)     # set型オブジェクトから特定の要素を削除するには、removeメソッドを使います。
# print(s)

# To define empty set,
s=set()
print(type(s))
print(s)