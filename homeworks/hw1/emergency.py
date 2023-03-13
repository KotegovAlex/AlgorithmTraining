k1, m, k2, p2, n2 = map(int, input().split())

k0 = k2 / n2
if k0 <= 1:
    p1 = 0
    n1 = 0
else:
    k0 = int(k2 / n2) + 1
    p1 = int(k1 / (m * k0)) + 1
    n1 = int((k1 - (p1 - 1) * (m * k0)) / k0) + 1

print(k0)
print(p1, n1)