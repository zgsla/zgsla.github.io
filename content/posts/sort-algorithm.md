---
title: "十大经典排序算法"
date: 2022-08-09T19:11:54+08:00
description: ""
type: "post"
tags: ["排序算法", "Python"]
draft: false
---

排序算法是《数据结构与算法》中最基本的算法之一。


<style type='text/css'>
    table th,
    table td{
        padding: 10px
    }
    .tb-content{
        background-color: #F5DEB3
    }
    .tb-title2{
        background-color: #87CEFA
    }
</style>

<table border='1'>
	<tr>
	    <th colspan="7" style='text-align: center; background-color: #90EE90' >十大经典排序算法对比</th>
	</tr >
	<tr style='heigth: 15px; background-color: #90EE90'>
	    <th rowspan='2' width='15%'>排序算法</td>
	    <th colspan='3' width='45%' style='text-align: center'>时间复杂度</td>
	    <th rowspan='2' width='15%'>空间复杂度</td> 
        <th rowspan='2' width='15%'>排序方式</td>
        <th rowspan='2' width='10%' style='text-align: center'>稳定性</td>
	</tr>
	<tr style='heigth: 15px; background-color: #90EE90'>
	    <th style='text-align: center'>平均</td>
	    <th style='text-align: center'>最好</td>
	    <th style='text-align: center'>最坏</td>
	</tr>
	<tr style='heigth: 5px'>
	    <td class='tb-title2'><a href='/algorithm/bubble'>冒泡排序</a></td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n)$</td>
        <td class='tb-content'>$O(n^2)$  </td>
        <td class='tb-content'>$O(1)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
	<tr>
	    <td class='tb-title2'><a href='/algorithm/select'>选择排序</a></td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(1)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>×</td>
	</tr>
	<tr>
	    <td class='tb-title2'><a href='/algorithm/insert'>插入排序</a></td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(1)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
	<tr>
	    <td class='tb-title2'><a href='/algorithm/shell'>希尔排序</a></td>
        <td class='tb-content'>$O(n^{1.3})$</td>
        <td class='tb-content'>$O(n)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(1)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>×</td>
	</tr>
	<tr>
	    <td class='tb-title2'><a href='/algorithm/merge'>归并排序</a></td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n)$</td>
        <td class='tb-content'>外部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
	<tr>
	    <td class='tb-title2'><a href='/algorithm/quick'>快速排序</a></td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>×</td>
	</tr>
    <tr>
	    <td class='tb-title2'><a href='/algorithm/heap'>堆排序</a></td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(n\log_2n)$</td>
        <td class='tb-content'>$O(1)$</td>
        <td class='tb-content'>内部排序</td>
        <td class='tb-content' style='text-align: center'>×</td>
	</tr>
    <tr>
	    <td class='tb-title2'><a href='/algorithm/count'>计数排序</a></td>
        <td class='tb-content'>$O(n+k)$</td>
        <td class='tb-content'>$O(n+k)$</td>
        <td class='tb-content'>$O(n+k)$</td>
        <td class='tb-content'>$O(k)$</td>
        <td class='tb-content'>外部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
    <tr>
	    <td class='tb-title2'><a href='/algorithm/bucket'>桶排序</a></td>
        <td class='tb-content'>$O(n+k)$</td>
        <td class='tb-content'>$O(n+k)$</td>
        <td class='tb-content'>$O(n^2)$</td>
        <td class='tb-content'>$O(n + k)$</td>
        <td class='tb-content'>外部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
    <tr>
	    <td class='tb-title2'><a href='/algorithm/radix'>基数排序</a></td>
        <td class='tb-content'>$O(n×k)$</td>
        <td class='tb-content'>$O(n×k)$</td>
        <td class='tb-content'>$O(n×k)$</td>
        <td class='tb-content'>$O(n + k)$</td>
        <td class='tb-content'>外部排序</td>
        <td class='tb-content' style='text-align: center'>√</td>
	</tr>
</table>  

**详细说明及代码实现如下：**  
1. [<font color="blue">冒泡排序</font>](/algorithm/bubble/)
2. [<font color="blue">选择排序</font>](/algorithm/select/)
3. [<font color="blue">插入排序</font>](/algorithm/insert/)
4. [<font color="blue">希尔排序</font>](/algorithm/shell/)
5. [<font color="blue">快速排序</font>](/algorithm/quick/)
6. [<font color="blue">归并排序</font>](/algorithm/merge/)
7. [<font color="blue">堆排序</font>](/algorithm/heap/)
8. [<font color="blue">计数排序</font>](/algorithm/count/)
9. [<font color="blue">桶排序</font>](/algorithm/bucket/)
10. [<font color="blue">基数排序</font>](/algorithm/radix/)