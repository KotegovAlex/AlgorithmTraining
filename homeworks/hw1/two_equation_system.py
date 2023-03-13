a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == c:
    if b == d:
        if f != e:
            print(0)
        elif f == e:
            print(5)
    elif b != d:
        print(4, (e - f) / (b - d))
elif b == d and a != c:
    print(3, (e - f) / (a - c))
elif b == 0 and c == 0:
    print(2, e / a, f / d)
elif a != c and b != d and f != e:
    print(1, (c - a) / (b - d), (e - f) / (b - d))
