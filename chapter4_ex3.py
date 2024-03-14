### 4-3 ３つの必須引数と２つのオプション引数がある関数
def three_plus_two_function(a,b,c,d=4,e=5):
    result = a*b*c+d+e
    """ Returns a*b*c+d+e
    :param a: float
    :param b: float
    :param c: float
    :param d (optinal): float
    :param e (optiona): float
    :return: float a*b*c+d+e
    """
    
    print(result)
    return(result)

three_plus_two_function(1,2,35,7,2)
