def matrix(mat, r, c):
    n, m = len(mat[0]), len(mat)
    t = r*c
    if n*m != t:
        return mat
    k = 0
    output = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(m):
        for j in range(n):
            output[k//c][k % c] = mat[i][j]
            k += 1
    return output


mat = [[1, 2], [3, 4]]
r = 2
c = 4
print(matrix(mat, r, c))
