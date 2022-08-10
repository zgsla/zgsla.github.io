def mat_sqrt(m, mod):
        return [
            [
                (m[0][0]*m[0][0] + m[0][1] * m[1][0]) % mod,
                (m[0][0]*m[0][1] + m[0][1] * m[1][1]) % mod,
            ],
            [
                (m[1][0]*m[0][0] + m[1][1] * m[1][0]) % mod,
                (m[1][0]*m[0][1] + m[1][1] * m[1][1]) % mod,
            ]
        ]

def mat_mul(m, n, mod):
    return [
        (m[0]*n[0][0] + m[1] * n[1][0]) % mod,
        (m[0]*n[0][1] + m[1] * n[1][1]) % mod
    ]

def fib(n):
    mod = 1000000007
    if n < 0:
        return
    elif n <= 2:
        return 1
    mat = [1, 1]

    q_matrix = [
        [0, 1],
        [1, 1]
    ]
    bin_n = bin(n - 2)[2:]
    matrixs = []
    
    for i in range(len(bin_n)):
        matrixs.insert(0, q_matrix)
        q_matrix = mat_sqrt(q_matrix, mod)

    for j, sbin in enumerate(bin_n):
        if sbin == '1':
            mat = mat_mul(mat, matrixs[j], mod)
    return mat[1]
for i in range(1, 10000000):
    print(fib(i))