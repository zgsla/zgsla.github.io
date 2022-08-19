---
title: "堆排序"
date: 2022-08-19T11:34:48+08:00
description: "堆排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---
## 前言  
堆排序是利用堆的数据结构完成排序的一种算法，堆可以理解为将它所有元素按照一个完全二叉树的顺序存储在数组中。  
堆分为最大堆和最小堆，所有元素都小于它根节点的为最大堆。  
因为元素都在数组中，所以元素$k_n$的左右子节点分别为$k_{2n+1}$和$k_{2n+2}$  

## 核心思想

1、构建最大堆（从树的的最后一个非叶子节点元素到第一个元素，比较它和它左右子节点的值叶子节点小则交换位置）  
2、步骤一完成后序列已满足最大堆，交换堆顶和堆尾元素，堆长度向后减少1，重复步骤一，直到堆没有叶子节点
3、如果一次循环中未发生元素交换，则序列已有序，可提前结束循环。  
```python
def heap_sort(lst):
    length = len(lst)
    while length > 1:
        for root in range(length // 2, -1, -1):
            left = 2 * root + 1
            right = 2 * root + 2

            if left < length and lst[left] > lst[root]:
                lst[root], lst[left] = lst[left], lst[root]

            if right < length and lst[right] > lst[root]:
                lst[root], lst[right] = lst[right], lst[root]
        length -= 1
        lst[0], lst[length] = lst[length], lst[0]
```
时间复杂度：  
&nbsp; &nbsp; 最优：$O(n\log_2n)$  
&nbsp; &nbsp; 最坏：$O(n\log_2n)$   
&nbsp; &nbsp; 平均：$O(n\log_2n)$   
空间复杂度： $O(1)$  
稳定性： 不稳定

Python 已提供内建库[heapq](https://docs.python.org/zh-cn/3.7/library/heapq.html)实现了堆数据结构以及相关操作