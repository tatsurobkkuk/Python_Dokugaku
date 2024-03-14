# 第１３章　オブジェクト指向プログラミングの４大要素

# 4大要素：カプセル化、抽象化、ポリモーフィズム、継承

## 1. カプセル化：2つの概念から成り立つ。
# （１）オブジェクトによって複数の変数とメソッドをまとめること。
# （２）データをクラス内に隠蔽して外から見えないようにすること。
# クラスの外側からオブジェクトを利用するコードをclientという。
# 例

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

# i) インスタンス変数numsを直接変更する方法
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

# ii) change_dataメソッドを使う方法
data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

# Pythonではプライベート変数はないが、clientからアクセスして欲しくない
# 変数やメソッドには、名前の前にアンダースコア_ を１つ付ける。変数やメソッドが
# アンダースコアで始まっていたら、触ってはいけない。

## 2.　抽象化
#　抽象化とは、対象から扱いたい問題にフォーカスして本質的な特徴だけを集めた状態
# にすること。

## 3. ポリモーフィズム
# ポリモーフィズムは、同じインターフェイスでありながらデータ型に合わせて異なる
# 動作をする機能

## 4. 継承
## 継承とはクラスを作るときに他のクラスからメソッドや変数を受け継ぐこと
# 例：図形を表すクラス

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

# my_shape = Shape(20, 25)
# my_shape.print_size()

# Shapeの子クラスを定義
# class Square(Shape):
#     pass ## 何もしなくて良いことを伝える
#
# a_square = Square(20, 20)
# a_square.print_size()

class Square(Shape):
    def area(self):
        return self.width*self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
print(a_square.area())
a_square.print_size()

## コンポジション
# コンポジションは「has-a関係」を表し、別クラスのオブジェクトを変数として
# 持たせる。

# 例：犬とその飼い主の関係をクラスで定義して、犬と人間の関係を表現する。
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)








