# 第１4章　もっとオブジェクト指向プログラミングの４大要素

#　おさらい
# すべてのオブジェクトはクラスのインスタンスである。
# クラスから作られるオブジェクトをインスタンスとよぶ。
# 本書の文脈では、オブジェクトと言った時はインスタンスのことを指す。

## クラス変数 vs.インスタンス変数
# Pythonではクラスそのものもオブジェクトとして扱え、その場合「クラスオブジェクト」と呼ぶ。

# 例：Squareというクラスオブジェクトを出力する
class Square:
    pass

print(Square)

## クラスには、クラス変数とインスタンス変数の２種類あり、self.[variable name] = [value]の
# ように書く変数はインスタンス変数であり、インスタンス変数はインスタンスオブジェクトに属する。

class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

## 特殊メソッド
# Pythonの全てのクラスはオブジェクトクラスを継承する。よって、オブジェクトから継承したメソッドを使うこと
# ができる。

# 例：クラスから作成してインスタンスオブジェクトをprint関数に渡す。
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

# 例；__add__メソッドをクラスに持たせて、そのオブジェクトを足し算の演算子で計算する。
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x+y)

# is
# is キーワードは、前後のオブジェクトが同一のオブジェクトならTrueを返す。同じでないなら、Falseを返す。
class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# is キーワードは、ある変数がNoneかどうかを調べるときにも使う。
x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None :( ")
else:
    print("x is not None")




