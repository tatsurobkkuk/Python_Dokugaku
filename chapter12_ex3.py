### Ex 3. 三角形を表すTriangleクラスを定義して、面積を返す
### areaメソッドを持たせよう。そしてTriangleオブジェクトを作って、
### areaメソッドを呼び出して、結果を出力しよう。

import math
class Triangle():
    def __init__(self, a, b, c):
        """ a, b, and c are triangle lengths"""
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Calculating area via Heron"s formula"""
        s = (self.a + self.b + self.c) * 0.5
        S = (s * (s - self.a) *  (s - self.b) * (s - self.c))**0.5
        return S

# Test code
triag1 = Triangle(5, 7, 3)
print("Area of Triangle:", triag1.area())