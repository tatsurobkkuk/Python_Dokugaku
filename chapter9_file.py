import os

os.path.join("Users",
             "tatsurotanioka",
             "Library",
             "Mobile Documents",
             "com~apple~CloudDocs",
             "Learning",
             "Python_Dokugaku",
             "st.txt")

# ファイルに書き出す
st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

# ファイルに書き出す（日本語）
st = open("st_jpn.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは！")
st.close()

# ファイルを自動的に閉じる
with open("st.txt", "w") as f:
    f.write("Hi from Python!")

# ファイルから読み込む
with open("st.txt", "r") as f:
    print(f.read())

# ファイルから読み込む（日本語）
with open("st_jpn.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ファイルから読み込んでリストに入れておく
my_list = []
with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

# csvファイルに書き出す
import csv
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter = ",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

# csvファイルを読み込む
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(",".join(row))











