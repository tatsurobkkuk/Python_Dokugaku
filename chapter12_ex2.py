### Ex 2. 円を表すCircleクラスを定義しよう。そのクラスに面積を計算して
### 返すメソッドareaを持たせよう。面積の計算には、Pythonの組み込みモジュール
### mathのpi定数が使えます。次に、Circleオブジェクトを作って、areaメソッドを
### 呼び出し、結果を出力しよう。
import math
class Circle():
    def __init__(self, radius):
        """ radius is in meters"""
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Test code
circ1 = Circle(10)
print("Area of circle with radius", circ1.radius, "is:", circ1.area())
