def create_box(m, n):
    matrix = [[1] * m for i in range(n)]
    c = 1
    for k in range(m // 2 + 1):
        for i in range(c - 1, n - c + 1):
            for j in range(c - 1, m - c + 1):
                matrix[i][j] = c
        c += 1
    for i in range(len(matrix)):
        print(matrix[i])
create_box(5, 8)