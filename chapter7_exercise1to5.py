### Ex 1. リストの要素をそれぞれ出力しよう。
# drama_list = ["Walking Dead",
#               "Entourage",
#               "The Sopranos",
#               "Vampire Diaries"]
# for drama in drama_list:
#     print(drama)

### Ex 2. 25から50までの数値をそれぞれ出力しよう
## Method 1.
# for i in range(25,51):
#     print(i)
## Method 2.
# x = 25
# while x < 51:
#     print(x)
#     x +=1

### Ex 3. チャレンジ１のリストの要素をそれぞれ、インデックス値と一緒に出力しよう
# drama_list = ["Walking Dead",
#               "Entourage",
#               "The Sopranos",
#               "Vampire Diaries"]
# index = 0
# for drama in drama_list:
#     print(index, drama)
#     index +=1

## solution
# drama_list = ["Walking Dead",
#               "Entourage",
#               "The Sopranos",
#               "Vampire Diaries"]
# for index, drama in enumerate(drama_list):
#     print(index, drama)


### Ex 4. 無限ループする数字当てプログラムを書こう
# answers = [1.0,3.0,6.0,11.0,34,220]
# i = input("Write a number to guess or press q to quit:")
# while True:
#     try:
#         val = float(i)
#         if val not in answers:
#             print("Wrong answer!")
#         elif val in answers:
#             print("Correct answer!")
#     except ValueError:
#         if i == "q":
#             break
#     i = input("Write a number to guess or press q to quit:")

## soltion
# answers = [1.0,3.0,6.0,11.0,34,220]
# while True:
#     i = input("Guess a number or type q to quit.")
#     if i == "q":
#         break
#     try:
#         i = int(i)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if i in answers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly!")

### Ex 5. 2つのリストに含まれる全ての数字の組み合わせで掛け算しよう。
# list1 = [8, 19, 148, 4]
# list2 = [9, 1, 33, 83]
# multiplied = []
# for i in list1:
#     for j in list2:
#         multiplied.append(i*j)
#
# print(multiplied)
