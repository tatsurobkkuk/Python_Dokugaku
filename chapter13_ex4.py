# 第１３章　オブジェクト指向プログラミングの４大要素

## チャレンジ 4：HorseクラスとRiderクラスを定義しよう。コンポジションを使って、馬（Horse)に
# 騎手(Rider)を持たせよう。

class Horse:
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

hitoshi = Rider("Hitoshi Matoba")
wonder = Horse("Grass Wonder", "Thoroughbred", hitoshi)

print("The name of Horse is {}.".format(wonder.name))
print("The name of Rider is {}.".format(wonder.rider.name))








