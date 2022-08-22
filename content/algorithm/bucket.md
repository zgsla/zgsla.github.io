---
title: "桶排序"
date: 2022-08-19T17:56:09+08:00
description: "桶排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---


设置固定数量的空桶；  
把数据放到对应的桶中；  
对每个不为空的桶中数据进行排序；   
拼接不为空的桶中数据，得到结果。 

---
```python
def bucket_sort(lst):
    max_value = lst[0]
    min_value = lst[0]
    for m in lst:
        if m > max_value:
            max_value = m
        if m < min_value:
            min_value = m

    # 1. 创建桶（注意：一个桶就是一个列表）
    bucket_num = (max_value - min_value) // 3 + 1
    buckets = [[] for _ in range(bucket_num)]
    # 2. 将数据分桶 并在桶内并排序
    for k in lst:  # 遍历列表中所有的数
        i = k // 3  # i 表示 放到几号桶里
        buckets[i].append(k)  # 将数添加到桶里边
        # 桶内排序 这里是插入排序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break

    prev_length = 0
    for i in range(bucket_num):
        cur_length = len(buckets[i])
        for j in range(cur_length):
            lst[i * prev_length + j] = buckets[i][j]
        prev_length = cur_length
```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n+k)$  
&nbsp; &nbsp; 最坏：$O(n^2)$   
&nbsp; &nbsp; 平均：$O(n+k)$   
空间复杂度： $O(n + k)$  
稳定性： 稳定