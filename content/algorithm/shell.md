---
title: "希尔排序"
date: 2022-08-18T18:44:42+08:00
description: "希尔排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

## 核心思想
1、将序列按固定步长分组，组内进行插入排序
2、缩小步长，重复步骤一，直到步长小于等于1

```python
def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
                else:
                    break
        gap = gap // 2
```

时间复杂度：  
&nbsp; &nbsp; 最优：$O(n)$  
&nbsp; &nbsp; 最坏：$O(n^2)$  
&nbsp; &nbsp; 平均：$O(n^{1.3})$  
空间复杂度： $O(1)$  
稳定性： 不稳定