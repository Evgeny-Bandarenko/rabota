# Hometask_13_2
# Напишите функцию f(x), которая возвращает значение следующей
# функции, определённой на всей числовой прямой:

# def f(x):
#     if x <= -2:
#         return 1 - ((x+2)2)
#     elif - 2 < x <= 2:
#         return -x / 2
#     else:
#         return (x - 2)  2 + 1
#
# print(f(4.5))


# Hometask_13_3
# Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два. In: 852 85 784 58 Out: [852, 784, 58]


# def modify_list(l):
#     i, n = 0, len(l)
#     while i < n:
#         if l[i] % 2:
#             l.pop(i)
#             n -= 1
#         else:
#             l[i] = l[i] // 2
#             i += 1
#
#
# l = [852, 85, 784, 58]
# modify_list(l)
# print(l)


# Из полученного списка чисел
# создайте список с суммами
# этих чисел, отсортированными
# по возрастанию

def listsum(numlist):
    thesum = 0
    for i in numlist:
        thesum = thesum + i
    return thesum

print(listsum([965, 582, 23,8, 695210]))
