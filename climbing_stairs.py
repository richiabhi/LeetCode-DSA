dic = {}


def climb(n):
    if n == 0 or n == 1:
        return 1
    if n in dic:
        return dic[n]
    res = climb(n-1) + climb(n-2)
    dic[n] = res
    return res


n = int(input())
print(climb(n))
