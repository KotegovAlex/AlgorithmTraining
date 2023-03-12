# Случай, когда переменная ans не инициализирована, программа упадет при вводе пустой строки в input():
def count_symbol():
    s = input()
    anscnt = 0
    symcnt = {}
    for now in s:
        if now not in symcnt:
            symcnt[now] = 0
        symcnt[now] += 1
    for key in symcnt:
        if symcnt[key] > anscnt:
            ans = now
            anscnt = symcnt[key]

    print(ans)


# Сумма последовательности с проверкой на пустую последовательность:
def seq_summ1():
    seq = list(map(int, input().split()))
    if len(seq) == 0:
        print(0)
    else:
        seqsum = seq[0]
        for i in range(1, len(seq)):
            seqsum += seq[i]
        print(seqsum)


# Более изящное решение, если объявить сразу переменную seqsum = 0
def seq_summ2():
    seq = list(map(int, input().split()))
    seqsum = 0
    for i in range(len(seq)):
        seqsum += seq[i]
    print(seqsum)


# Максимум последовательности:
def seq_max1():
    seq = list(map(int, input().split()))
    seqmax = 0
    for i in range(len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
    print(seqmax)


# Максимум последовательности:
def seq_max2():
    seq = list(map(int, input().split()))
    if len(seq) == 0:
        print('-inf')
    else:
        seqmax = seq[0]
        for i in range(1, len(seq)):
            if seq[i] > seqmax:
                seqmax = seq[i]
    print(seqmax)


if __name__ == '__main__':
    pass
