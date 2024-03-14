# for i in range(0,100):
#     print(i)
#     break

# qs = ["What is your name?",
#       "What is your fav. color?",
#       "What is your quest?"]
# n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == "q":
#         break
#     n = (n + 1) % 3

# continue文
# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# # 入れ子のループ 1.
# for i in range(1, 3):
#     print(i)
#     for letter in ["a", "b", "c"]:
#         print(letter)

# 入れ子のループ　2.
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# added = []
# for i in list1:
#     for j in list2:
#         added.append(i+j)
#
# print(added)

# 入れ子のループ 3.
while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)










