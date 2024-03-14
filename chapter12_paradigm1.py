### 手続型プログラミング：データをグローバル変数としてもち、関数でそのデータを操作する。
# 手続型プログラミングでは複数の手続き（関数）にまたがって同じデータを扱いたい場合にグローバル変数で
# データを管理できるため、一歩間違えると予期しないエラーが発生しやすい。

# 例
pop = []   #　洋楽ポップソングを保存するリスト
jpop = []  # JPopソングを保存するリスト

def collect_songs():
    song = "曲名を入力してください： "
    ask = "p　か j のどちらかを入力してください。qで終わります："

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("不正な値です。")
            print("pop songs:", pop)
            print("jpop songs:", jpop)

collect_songs()