# 打印三角形图案
row = int(input('请输入行数：'))

for i in range(row):
    for _ in range(i + 1):# 在循环中，如果你不需要迭代变量的值，可以使用 _ 作为占位符，从而告诉阅读代码的人，迭代变量的值不会被使用
        print('*',end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ',end = '')
        else:
            print('*',end = '')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

