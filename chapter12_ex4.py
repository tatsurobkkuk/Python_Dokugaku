### Ex 4. 六角形を表すHexagonクラスを定義して、外周を返す
### calculate_perimeterメソッドを持たせよう。そしてHexagon
### オブジェクトを作って、calculate_perimeterメソッドを呼び出して、
### 結果を出力しよう。

import math
class Hexagon():
    def __init__(self, a, b, c, d, e, f):
        """ a, b, ...,e are hexagon lengths"""
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def calculate_perimeter(self):
        """Calculating perimeter"""
        return self.a + self.b + self.c + self.d + self.e + self.f

# Test code
hex1 = Hexagon(5, 7, 3, 5, 6, 7)
print("Perimeter of hexagon:", hex1.calculate_perimeter())