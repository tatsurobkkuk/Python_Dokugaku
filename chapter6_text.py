""" line one
    line two
    line three
"""

what = input("何が：")
when = input("いつ：")
where = input("どこで：")
do = input("どうした：")

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)

words = ["The", "fox", "jumped",
         "over", "the", "fence", "."]
one = " ".join(words)
one

try:
    "animals".index("z")
except:
    print("Not found.")