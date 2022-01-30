def triangle(array):
    n = len(array)
    for r in range(n-2, -1, -1):
        for c in range(r+1):
            array[r][c] += min(array[r+1][c], array[r+1][c+1])
    return array[0][0]


arr = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(triangle(arr))
