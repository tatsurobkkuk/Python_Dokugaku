### Chapter 17: 正規表現

import re
l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

# print(matches)

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l, re.IGNORECASE)

# print(matches)

zen = """Although never is 
often better than 
*right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation is 
easy to explain, 
it may be a good 
idea. Namespaces 
are one honking 
great idea -- let's 
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
# print(m)

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
# print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
# print(m)

t = "__one__ __two__ __three__ "
found = re.findall("__.*?__", t)
# for match in found:
#     print(match)

# Mad Libs ゲーム
text = """キリンは大昔から__複数名詞__の興味の対象でした。キ
リンは__複数名詞__の中で一番背が高いですが、科学者はそのよ
うな長い__体の一部__をどうやって獲得したのか説明できません。キ
リンの身長は__数値__ __単位__近くあり、その高さのほとんどは脚
と__体の一部__によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語（＝
    ヒント）の部分は後を２つのアンダースコアで挟んでください。ヒントの単
    語にはアンダースコアを含めないでください。__hint_hintはだめで
    す。__hint__はokです。
    :return:
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

# mad_libs(text)

line = "I love $"
m =re.findall("\\$", line, re.IGNORECASE)
print(m)












