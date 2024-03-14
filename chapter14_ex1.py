# 第１4章　もっとオブジェクト指向プログラミングの４大要素

## Challenge 1: Squareクラスにsquare_listクラスを追加しよう。そして、新しくSquare
# クラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。
class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self.len)

    def print_size(self):
        return "Square of length {}".format(self.len)

    def calculate_perimeter(self):
        return 4 * self.len

    def change_method(self, value):
        self.len += value

s1 = Square(10)
s2 = Square(20)
s3 = Square(30)

print(Square.square_list)
