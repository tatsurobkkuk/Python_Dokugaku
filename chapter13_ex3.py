# 第１３章　オブジェクト指向プログラミングの４大要素

## チャレンジ　3 ：Shapeクラスを定義しよう。呼ばれたら"I am a Shape"を返すメソッド what_am_iを
# 定義しよう。前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させ
# よう。そしてRectangleとSquareのオブジェクトを生成して、このチャレンジで追加したメソッドwhat_am_i
# を呼んでみよう。

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        return "{} by {}".format(self.width, self.len)

    def calculate_perimeter(self):
        return 2 * self.len + 2 * self.width

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def print_size(self):
        return "Square of length {}".format(self.len)

    def calculate_perimeter(self):
        return 4 * self.len

    def change_method(self, value):
        self.len += value

a_square = Square(20)
print("my shape is", a_square.print_size(), ",",
      "perimeter is", a_square.calculate_perimeter())
a_square.what_am_i()

a_rectangle = Rectangle(20, 30)
print("my shape is", a_rectangle.print_size(), ",",
      "perimeter is", a_rectangle.print_size())
a_rectangle.what_am_i()
