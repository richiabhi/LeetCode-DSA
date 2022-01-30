def rob(arr):
    prev = 0
    curr = 0
    for val in arr:
        temp = prev
        prev = curr
        curr = max(val+temp, prev)
    return curr


arr = list(map(int, input().split()))
print(rob(arr))
