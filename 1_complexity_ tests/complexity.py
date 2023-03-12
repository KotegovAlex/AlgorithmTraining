# Два вложенных цикла O(n^2)
# 100*N = O(N)
# Пространственная сложность - количество используемой памяти

# Заданча 1. Найти самый часто встречающийся символ в строке
# Решение 1 (O(N^2)) через вложенный цикл:
def symbol1():
    s = input()
    ans = ''
    anscnt = 0
    for i in range(len(s)):
        nowcnt = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                nowcnt += 1
        if nowcnt > anscnt:
            ans = s[i]
            anscnt = nowcnt

    print(ans)


# Решение 2 (O(k*N)) c помощью множества:
def symbol2():
    s = input()
    ans = ''
    anscnt = 0
    for now in set(s):
        nowcnt = 0
        for j in range(len(s)):
            if now == s[j]:
                nowcnt += 1
        if nowcnt > anscnt:
            ans = now
            anscnt = nowcnt

    print(ans)


# Решение 3 (O(N + k)) с помощью словаря:
def symbol3():
    s = input()
    ans = ''
    anscnt = 0
    dct = {}
    for now in s:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for key in dct:
        if dct[key] > anscnt:
            ans = key
            anscnt = dct[key]

    print(ans)


if __name__ == '__main__':
    pass
