# Ex 1. statisticsモジュールの別の関数を呼んでみよう
import statistics

# StDev
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.stdev(nums))

# Geometric mean
print(statistics.geometric_mean(nums))

# Ex 2. cubedという名前のモジュールを作り、渡された数値を３乗して返そう
import cubed
x = 3
y = cubed.cubed(3)
print(y)
