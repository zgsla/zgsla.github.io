from ast import mod


def fib(n):

    if n < 0:
        return
    
    mat = [1, 1]

    mod_matrix = [
        [0, 1],
        [1, 1]
    ]

    def mat_sqrt(m):
        return [
            [
                m[0][0]*m[0][0] + m[0][1] * m[1][0],
                m[0][0]*m[0][1] + m[0][1] * m[1][1],
            ],
            [
                m[1][0]*m[0][0] + m[1][1] * m[1][0],
                m[1][0]*m[0][1] + m[1][1] * m[1][1],
            ]
        ]
    
    def mat_mul(m, n):
        return [
            m[0]*n[0][0] + m[1] * n[1][0],
            m[0]*n[0][1] + m[1] * n[1][1]
        ]

    bin_n = bin(n - 2)[2:]
    print(bin_n)
    matrixs = []

    for i in range(len(bin_n)):
        matrixs.insert(0, mod_matrix)
        # print(mod_matrix)
        mod_matrix = mat_sqrt(mod_matrix)
    # print(matrixs)
    for j, sbin in enumerate(bin_n):
        if sbin == '1':
            mat = mat_mul(mat, matrixs[j])
    return mat[1]

print(fib(10**10))