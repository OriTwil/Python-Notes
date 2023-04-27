# exp1
f_exp1 = float(input('F = '))
c_exp1 = (f_exp1 - 32) / 1.8
print('%.2fF = %.2fC' % (f_exp1,c_exp1))

# exp2
year = int(input("year : "))
is_leap = year % 4 == 0 and year % 100 != 0 \
        or year % 400 == 0
print(is_leap)
