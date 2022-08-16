---
title: "Insert"
date: 2022-08-16T17:42:07+08:00
description: "插入排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

### 核心思想

1、定义一个已排序序列（初始一般指定第一个元素），将已排序序列后一个元素与已排序序列中每个元素从后往前比较，如果未排序元素小则交换，否则说明已经到正确位置，终止循环。  
2、已排序序列范围向后增加1，重复步骤2，直到已排序序列长度等于原序列长度

```python
def insert_sort(lst):
    """定义一个已排序序列，将剩余未排序序列依次插入到已排序序列"""
    n = len(lst)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
```

时间复杂度：  
&nbsp; &nbsp; 最优：$O(n)$  
&nbsp; &nbsp; 最坏：$O(n^2)$  
&nbsp; &nbsp; 平均：$O(n^2)$

稳定性： 稳定