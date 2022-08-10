---
title: "Fibonacci"
date: 2022-08-09T19:11:54+08:00
description: "斐波那契求第n项，n为指数级大数"
type: "post"
tags: ["fibnacci", "10**19", "斐波那契"]
draft: false
---

# 斐波那契数列求第n项


1、1、2、3、5、8、13 ······  

下面是简单的python实现
```python
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
可以看出，上面的时间复杂度是`O(n)`,可以算是比较优的方式了  

现在有个新的需求，求第`10**19`项，由于结果巨大，输出mod 1000000007的结果即可，我尝试在自己的电脑上运行，它很长时间都没有给我结果。

如果需要计算的n为特别大，有没有减少运算次数的方式呢？  

答案是有的，需要使用[斐波那契Q矩阵](https://mathworld.wolfram.com/FibonacciQ-Matrix.html)  

<!-- 现在重新回顾一下斐波那契数列的定义；前两项为1，从第三项开始都满足下面的公式
$$k_n = k_{n-1} + k_{n-2}$$   -->

<!-- 可以发现，如果仅仅已知第n-1项，无法求出第n项的值  


如果将相邻两项组组合成shape为[1,2]的矩阵，并重新定义为序列$s_n$，序列拥有下面的规律  
$s_1 = \\begin{bmatrix}k_1&k_2\\end{bmatrix}=\\begin{bmatrix}k_1&k_2\\end{bmatrix}$  
$s_2 = \\begin{bmatrix}k_2&k_3\\end{bmatrix}=\\begin{bmatrix}k_2&k_1 + k_2\\end{bmatrix}$  
$s_3 = \\begin{bmatrix}k_3&k_4\\end{bmatrix}=\\begin{bmatrix}k_3&k_2 + k_3\\end{bmatrix}$  
···  
$s_{n-2} = \\begin{bmatrix}k_{n-2}&k_{n-1}\\end{bmatrix}=\\begin{bmatrix}k_{n-2}&k_{n-3}+k_{n-2}\\end{bmatrix}$  
$s_{n-1} = \\begin{bmatrix}k_{n-1}&k_n\\end{bmatrix} = \\begin{bmatrix}k_{n-1}&k_{n-2} + k_{n-1}\\end{bmatrix}$

那么新序列$s_n$在已知$s_{n-1}$的情况下是可以求出$s_n$的 -->

这里先介绍一下矩阵幂运算的概念，下面假设`A`是一个矩阵，则以下均成立

<!-- $$A^2 = A * A$$

$$A^4 = A^2 * A^2$$

$$A^7 = A^4 * A^2 * A^1$$ -->

`A ** 2` = `A` * `A`  
`A ** 4` = `A ** 2` * `A ** 2`  
`A ** 100` = `A ** 64` * `A ** 32` * `A ** 4`

还有一点 mod 运算也满足 `A * B mod C = (A mod C) * (B mod C)`

由于我们已经清楚了矩阵幂运算的规则，所以只需要找到一个矩阵`A`满足：  
[`kn-2` `kn-1`] * `A` = [`kn-1` `kn-2+kn-1`]
<!-- $
\\begin{bmatrix}
k_{n-2} & k_{n-1}
\\end{bmatrix} * A = \\begin{bmatrix}
k_{n-1} & k_{n-2} + k_{n-1}
\\end{bmatrix} 
$   -->


那么求第`n`项fib值就可以转化成求矩阵`A`的`n-2`次幂的问题了  
很容易可以推导出矩阵
`A`为 
```
[
    [0, 1], 
    [1, 1]
]
```
<!-- $A=\\begin{bmatrix}
0&1\\\\
1&1
\\end{bmatrix}$， -->
这样的`A`矩阵也被称为[斐波那契Q矩阵](https://mathworld.wolfram.com/FibonacciQ-Matrix.html)，可以应用于解决很多问题。

下面给出python的实现

```python
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

```

注1：*如果使用python，numpy已经提供了矩阵计算的方法，这里自己定义仅仅是为了演示，本文不提倡重复造轮子*  
注2：*纯python int原则上可以存储无限大，如果使用numpy 需要注意精度问题*