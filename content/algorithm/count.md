---
title: "Count"
date: 2022-08-19T14:37:12+08:00
description: "计数排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---
## 前言  
计数排序，桶排序，和基数排序都需要额外的数据结构来辅助排序  

```python
def count_sort(lst, min_value, max_value):
    # 获取所需桶的数量
    bucket_num = max_value - min_value + 1
    # 构建初始桶
    bucket = [0] * bucket_num
    # 统计元素数量，并存储在桶的对应位置
    for i in lst:
        bucket[i - min_value] += 1
    cur = 0
    # 将桶中元素依次放回原数组，覆盖原数组元素
    for j in range(bucket_num):
        for _ in range(bucket[j]):
            lst[cur] = j
            cur += 1
```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n+k)$  
&nbsp; &nbsp; 最坏：$O(n+k)$   
&nbsp; &nbsp; 平均：$O(n+k)$   
空间复杂度： $O(k)$  
稳定性： 稳定

额外提供一种稳定的计数排序Python实现

```python
def count_sort(lst, min_value, max_value):
    # 获取所需桶的数量
    bucket_num = max_value - min_value + 1
    # 构建初始桶
    bucket = [0] * bucket_num
    # 统计元素数量，并存储在桶的对应位置
    for i in lst:
        bucket[i - min_value] += 1

    for j in range(1, bucket_num):
        bucket[j] += bucket[j-1]
    result = [None] * len(lst)
    for k in range(len(lst) - 1, -1, -1):
        t = lst[k] - min_value
        bucket[t] -= 1
        result[bucket[t]] = lst[k]
    return result

```