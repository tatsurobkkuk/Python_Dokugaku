### Ex 1. リンゴと言われて思い浮かぶ4つの属性を考えよう。その4つの属性をインスタンス変数に持つ
### Appleクラスを定義しよう。

class Apple():
    def __init__(self, weight, color, variant, sweetness):
        """ weight is weight in grams,
        color, variant is the variant,
        s is the sweetness out of 10"""
        self.weight = weight
        self.color = color
        self.variant = variant
        self.sweetness = sweetness


# Testing the code out
ap1 = Apple(10, "red", "Honey Crisp", 7)
print((ap1.color, ap1.weight))

