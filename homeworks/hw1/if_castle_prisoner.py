a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > 0 and b > 0 and c > 0 and d > 0 and e > 0:
    if d >= a:
        if e >= b or e >= c:
            print('YES')
        else:
            print('NO')
    elif d >= b:
        if e >= a or e >= c:
            print('YES')
        else:
            print('NO')
    elif d >= c:
        if e >= a or e >= b:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')

