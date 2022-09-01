---
title: "归并排序"
date: 2022-08-18T18:50:49+08:00
description: "归并排序"
type: "page"
tags: ["排序算法", "python"]
draft: false
---

## 核心思想
1、递归分解序列至不可分  
2、合并序列，合并的同时对序列排序

```python
def merge_sort(lst):
    """
    递归分解序列至不可分，再递归合并，合并的同时对序列排序，
    使用两个指针分别遍历两个子序列，将元素按大小依次加入新的序列
    """
    n = len(lst)
    if n <= 1:
        return
    mid = n // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    left_idx = 0
    right_idx = 0
    lst[:] = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            lst.append(left[left_idx])
            left_idx += 1

        else:
            lst.append(right[right_idx])
            right_idx += 1
    lst += left[left_idx:]
    lst += right[right_idx:]
```

时间复杂度：  
&nbsp; &nbsp; 最优：$O(n\log_2n)$   
&nbsp; &nbsp; 最坏：$O(n\log_2n)$   
&nbsp; &nbsp; 平均：$O(n\log_2n)$   
时间复杂度： $O(n)$  
稳定性： 稳定