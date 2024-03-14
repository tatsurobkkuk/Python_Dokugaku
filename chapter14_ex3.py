# 第１4章　もっとオブジェクト指向プログラミングの４大要素
## Challenge 3:２つのパラメーターを受け取る関数を書こう。この関数は同じオブジェクト
# を渡されたらTrueを返し、そうではなかったらFalseを返そう。

def take_two_variables(x, y):
    if x is y:
        return True
    else:
        return False

print(take_two_variables(3, 3))
print(take_two_variables("a", "a"))
print(take_two_variables("a", "b"))

# alternative solution
def take_two_variables(x, y):
    return x is y

print(take_two_variables(3, 3))
print(take_two_variables("a", "a"))
print(take_two_variables("a", "b"))
