### 4-4 ２つの関数からなるプログラム。１つ目の関数は整数を引数として受け取り、その整数を２で割って求められる整数を出力として返す。
###      ２つ目の関数は整数を引数として受け取り、４でかけた整数を返す。

def divide_int_2(n):
    """ Returns n // 2
    :param n: int
    :returns: int n//2
    """
    n = int(n)
    result = n // 2
    return(result)

def multiply_by_4(n):
    """ Returns n*4
    :param n: int
    :returns: int n multiplied by 4
    """
    n = int(n)
    result = n*4
    return(result)

x = input("type a number:")
y = divide_int_2(x)
z = multiply_by_4(y)
print(z)
