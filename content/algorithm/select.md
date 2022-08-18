---
title: "Select"
date: 2022-08-16T17:31:02+08:00
description: "选择排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

### 核心思想

1、遍历序列找到最小元素并记录，将最小元素与队列首元素交换  
2、序列范围向前缩小1，重复步骤1

```python
def select_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
```

时间复杂度：  
&nbsp; &nbsp; 最优：$O(n^2)$  
&nbsp; &nbsp; 最坏：$O(n^2)$  
&nbsp; &nbsp; 平均：$O(n^2)$  
空间复杂度： $O(1)$  
稳定性： 不稳定