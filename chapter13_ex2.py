# 第１３章　オブジェクト指向プログラミングの４大要素

## チャレンジ2：Squareクラスにchange_methodメソッドを定義して、そこに渡した数値の分だけSquareオブジェクトの
# 横幅を増やしたり、減らしたり（マイナス値の場合）してみよう。

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        return "{} by {}".format(self.width, self.len)

    def calculate_perimeter(self):
        return 2 * self.len + 2 * self.width

class Square:
    def __init__(self, l):
        self.len = l

    def print_size(self):
        return "Square of length {}".format(self.len)

    def calculate_perimeter(self):
        return 4 * self.len

    def change_method(self, value):
        self.len += value

sq1 = Square(4)
print("Perimeter of Initial", sq1.print_size(),
      "is", sq1.calculate_perimeter())

change_amount = 3
sq1.change_method(change_amount)
print(f"Length of square after change by {change_amount} is", sq1.len,
      "and perimeter is", sq1.calculate_perimeter())