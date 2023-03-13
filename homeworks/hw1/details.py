# n, k, m = map(int, input().split())
# res = 0
#
# while n >= k:
#     k_num = n // k
#     m_num = k // m
#     res += m_num * k_num
#     ost = n - k_num * m_num * m
#     n = ost
#
# print(res)

N, K, M = map(int, input().split())


def details(n: int, k: int, m: int, res: int = 0) -> int:
    if n < k or m > k:
        return 0
    k_num = n // k
    m_num = k // m
    ost = n - k_num * m_num * m
    res = k_num * m_num
    res += details(ost, k, m, res)
    return res


print(details(N, K, M))
