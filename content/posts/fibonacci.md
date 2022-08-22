---
title: "Fibonacci"
date: 2022-08-09T19:11:54+08:00
description: "斐波那契求第n项，n为指数级大数"
type: "post"
tags: ["fibnacci", "10**19", "斐波那契"]
draft: false
---

### 定义  
前两项为1，从第三项开始都满足下面的公式  
$$k_n = k_{n-1} + k_{n-2}$$

例如 1、1、2、3、5、8、13 ······  

根据上面的定义给出下面简单的python实现
```python
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
可以看出，上面算法的时间复杂度是$O(n)$,可以算是比较优的方式了  

_现在有个新的需求，求第$10^{19}$项的值，由于结果巨大，输出$mod$ $1000000007$的结果即可，我尝试在自己的电脑上运行，它很长时间都没有给我结果。_

如果需要计算的$n$为特别大，有没有减少运算次数的方式呢？  

答案是有的，需要使用到[斐波那契Q矩阵](https://mathworld.wolfram.com/FibonacciQ-Matrix.html)  

这里先介绍一下快速幂运算的概念，则以下均成立

$x^2 = x × x$

$x^4 = x^2 × x^2$  

$x^4$的计算如果用一次项乘4次需要计算3次，但是如果先计算2次项的平方则只需要计算2次。  

同理 $x^{100} = x^{64} × x^{32} × x^4$  

实际操作中可以将低次项的结果保留起来，计算高次项时利用低次项的结果作为基础  

同时， $mod$运算也满足 $(A × B)$ % $C$ = $(A$ % $C)$ × $(B$ % $C)$

使用幂运算的规则，所以只需要找到一个数或者表达式 $A$ 满足： 

$$k_n = A × k_{n-1}$$  

那么求第$n$项$fibonacci$值的问题就可以转化成求 $A^{n-1}$的问题了 

但是通过$fibonacci$数列的定义可以知道，仅已知$k_{n-1}$无法确定$k_n$的值，必须要同时已知$k_{n-1}$和$k_{n-2}$才能确定$k_n$的值，即无法找到到 $A$ 满足$k_n = A × k_{n-1}$

### 重新定义序列

这里需要将原序列的相邻两项看作是一项，间隔为原序列的一项，组成新的序列满足  

$$s_n = (k_{n-1}, k_n)$$

即：常量或常量表达式$A$ 需要满足:  

$$s_n = A × s_{n-1}$$

也即为： 

$$(k_{n-1}, k_n) = A × (k_{n-2}, k_{n-1})$$  

又因为： 

$$k_n = k_{n-1} + k_{n-2}$$  

所以： 

$$(k_{n-1}, k_{n-2}+k_{n-1}) = A × (k_{n-2}, k_{n-1})$$

可以联想到矩阵的乘法，于是将上面最后的结果用矩阵乘法表达：  
$$
\begin{bmatrix}
k_{n-2} & k_{n-1}
\end{bmatrix} × A = \begin{bmatrix}
k_{n-1} & k_{n-2} + k_{n-1}
\end{bmatrix} 
$$

可以推导出：  
$$A=\begin{bmatrix}
0&1\\\\
1&1
\end{bmatrix}$$

这样的 $A$ 矩阵也被称为[斐波那契Q矩阵](https://mathworld.wolfram.com/FibonacciQ-Matrix.html)，可以应用于解决很多问题。

下面是使用上述方式的python实现

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
注2：*纯python int原则上可以存储无限大如果使用numpy 需要注意精度问题*