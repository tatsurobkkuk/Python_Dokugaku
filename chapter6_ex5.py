### Ex 5. リストの文字列を連結しよう。
words = ["The", "fox", "jumped",
         "over", "the", "fence", "."]
one = " ".join(words).replace(" .", ".")
print(one)