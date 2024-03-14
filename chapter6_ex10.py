### Ex 10. 文字列をスライスして、「、」の前までの文字列を作ろう。

string = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
partial_string = string[:string.index("、")]
print(partial_string)


