### Chapter 17: 正規表現
# Challenge 1. grep を使って、The Zen of Pythonの
# 文中にある”Dutch”という単語に一致する正規表現を書こう。
# grep Dutch. zen.txt

# Challenge 2. grep を使って、文字列 "The Arizona 479, 501,
# 870. California 209, 213, 650."にある、数字の部分全てに一致する
# 正規表現を書こう。
# echo "The Arizona 479, 501, 870. California 209, 213, 650." | grep "[[:digit:]]"

# Challenge 3. Pythonのreモジュールを使って、何かの文字の後にoが2回登場する
# 単語に一致する正規表現を書こう。そして、"The ghost says boo haunts the loo"
# の文中にあるbooやlooに一致するか試そう。
import re
t = "The ghost says boo haunts the loo."
m = re.findall(".oo", t, re.IGNORECASE)
print(m)