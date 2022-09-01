---
title: "冒泡排序"
date: 2022-08-16T17:11:26+08:00
description: "冒泡排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

## 核心思想

1、依次比较相邻元素，后面的比前面的小则交换元素，序列最后一个元素为最大元素  
2、遍历长度缩小1，重复步骤一  
3、如果一次循环中未发生元素交换，则序列已有序，可提前结束循环。  
```python
def bubble_sort(lst):
    n = len(lst)
    for j in range(1, n - 1):
        count = 0
        for i in range(n - j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                count += 1
        if count == 0:
            break
```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n)$  
&nbsp; &nbsp; 最坏：$O(n^2)$  
&nbsp; &nbsp; 平均：$O(n^2)$  
空间复杂度： $O(1)$  
稳定性： 稳定