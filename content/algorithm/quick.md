---
title: "快速排序"
date: 2022-08-16T17:59:35+08:00
description: "快速排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

### 核心思想

1、随机选择一个元素作为基准（一般选择第一个或最后一个元素），将序列按照基准切分成两份，大于基准的在后面，小于基准的在前面。  
2、递归对切分的序列进行步骤1，直到序列不可分

```python
def quick_sort(lst, head, tail):

    if head >= tail:
        return

    p = lst[head]
    start = head
    end = tail

    while start < end:

        while start < end and lst[end] >= p:
            end -= 1
        lst[start] = lst[end]

        while start < end and lst[start] <= p:
            start += 1
        lst[end] = lst[start]

    lst[end] = p

    quick_sort(lst, head, start - 1)
    quick_sort(lst, start + 1, tail)

```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n\log_2n)$  
&nbsp; &nbsp; 最坏：$O(n^2)$  
&nbsp; &nbsp; 平均：$O(n\log_2n)$  
空间复杂度： $O(n\log_2n)$   
稳定性： 不稳定