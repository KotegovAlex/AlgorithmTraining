a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (a == c and b == d and f != e) or (a == 0 and b == 0 and e != 0) or (c == 0 and d == 0 and f != 0):
    print(0)
elif a == c and b == d and f == e:
    print(5)
elif a == c and b != d:
    print(4, (e - f) / (b - d))
elif b == d and a != c:
    if e == f:
        print(3, 0.0)
    else:
        print(3, (e - f) / (a - c))
elif b == 0 and c == 0:
    print(2, e / a, f / d)
elif a == 0 and d == 0:
    print(2, f / c, e / b)
elif a != c and b != d and f != e:
    print(1, (c - a) / (b - d), (e - f) / (b - d))
