### 4-5 文字列をfloat型に変換して戻り値とする関数。起こりうる例外をキャッチする例外処理をかく
def string_to_float():
    """ Converts a text to float
    :input: number
    :returns: float a number converted from string to float
    """
    
    try:
        a = input("type a number:")
        result = float(a)
        print(result)
    except(ValueError):
        print("Invalid input")
        
string_to_float()
