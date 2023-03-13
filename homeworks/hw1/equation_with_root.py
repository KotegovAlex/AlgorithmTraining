a = int(input())
b = int(input())
c = int(input())

if c < 0 or a == 0 and (b < 0 or (b == 0 and c > 0) or (b > 0 and c == 0) or (b > 0 and c > 0 and b != c ** 2)):
    print('NO SOLUTION')
elif a == 0 and b == c ** 2:
    print('MANY SOLUTIONS')
else:
    x = (c ** 2 - b) / a
    if x == int(x):
        print(int(x))
    else:
        print('NO SOLUTION')


# def func(a, b, c):
#     if c < 0 or a == 0 and (b < 0 or (b == 0 and c > 0) or (b > 0 and c == 0) or (b > 0 and c > 0 and b != c ** 2)):
#         print('NO SOLUTION')
#     elif a == 0 and b == c ** 2:
#         print('MANY SOLUTIONS')
#     else:
#         x = (c ** 2 - b) / a
#         if x == int(x):
#             print(int(x))
#         else:
#             print('NO SOLUTION')
#
#
# func(1, 1, -1)
# func(0, -1, 1)
# func(0, 0, 1)
# func(2, 2, 3)
# func(0, 2, 0)
# func(0, 4, 2)
# func(0, 0, 0)
# func(0, 1, 1)
# func(1, 2, 3)
# func(0, 1, 2)
