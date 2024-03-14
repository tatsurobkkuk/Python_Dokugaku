# 第１３章　オブジェクト指向プログラミングの４大要素

## チャレンジ１：RectangleとSquareクラスを作ろう。両方のクラス
# にその図形の外周の長さを計算して返すcalculate_perimeterメソッド
# を定義しよう。そしてRectangleとSquareオブジェクトを作ってそれぞれ
# のcalculate_perimeterメソッドを呼ぼう。

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

rect1 = Rectangle(3,4)
print("Perimeter of Rectangle with dimension:", rect1.print_size(),
      "is", rect1.calculate_perimeter())
sq1 = Square(4)
print("Perimeter of ", sq1.print_size(),
      "is", sq1.calculate_perimeter())