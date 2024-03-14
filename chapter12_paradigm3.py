### オブジェクト指向プログラミング：関数の引数に状態を渡すのではなく、オブジェクトに状態を持たせる。
## 利点：開発や保守に係るトータルの時間が短縮されること。
## 欠点：プログラムを書く前の計画や設計などに、より多くの労力をかける必要があること。

## 例
class Orange:
    def __init__(self, w, c):
        """weight（重さ）はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

class Rectangle:
    def __init__(self, w , l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

or1 = Orange(10, "dark orange")
print(or1.mold)
or1.rot(10, 37)
print(or1.mold)
# インスタンス変数の値の変更
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)

# Orangeクラスを利用して、複数のオレンジオブジェクトを作る
or1 = Orange(4, "light orange")
or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())