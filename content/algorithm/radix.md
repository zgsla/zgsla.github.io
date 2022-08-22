---
title: "Radix"
date: 2022-08-19T18:14:17+08:00
description: "基数排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

```python

def radix_sort(lst, max_value):

    radix = 0
    while max_value:
        buckets = [[] for _ in range(10)]
        for i in lst:
            buckets[(i // (10 ** radix)) % 10].append(i)
        print(buckets)
        cur = 0
        for i in range(10):
            for j in buckets[i]:
                lst[cur] = j
                cur += 1
        max_value //= 10
        radix += 1

```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n×k)$   
&nbsp; &nbsp; 最坏：$O(n×k)$   
&nbsp; &nbsp; 平均：$O(n×k)$   
空间复杂度： $O(n + k)$  
稳定性： 稳定