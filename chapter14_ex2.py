# 第１4章　もっとオブジェクト指向プログラミングの４大要素

## Challenge 2: Squareクラスのオブジェクトをprint関数に渡したら、４辺それぞれの長さを出力
# しよう。

class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self.len)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len,self.len,self.len,self.len)

    def print_size(self):
        return "Square of length {}".format(self.len)

    def calculate_perimeter(self):
        return 4 * self.len

    def change_method(self, value):
        self.len += value

s1 = Square(29)
print(s1)