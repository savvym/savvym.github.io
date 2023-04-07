---
title: "[C++]advance(), prev() and next()"
date: 2022-06-20
summary: "C++ STL advance, prev() and next() 说明"
categories:
- C++
tags:
- C++
- STL
# hidemeta: true
---
> 定义在头文件 `<iterator>`

## std::advance

增加给定的迭代器 it 以 n 个元素的步长。  
若 n 为负，则迭代器自减。该情况下， InputIt 必须满足遗留双向迭代器 (LegacyBidirectionalIterator) 的要求，否则行为未定义。

### 参数
- **`it`** :	要前进的迭代器
- **`n`**   :	it 要前进的元素数

### 返回值
(无)

### 复杂度
线性。  
然而，若 InputIt 额外满足遗留随机访问迭代器 (LegacyRandomAccessIterator) 的要求，则复杂度是常数。

### 示例
Code:  
```C++
#include <iostream>
#include <iterator>
#include <vector>
 
int main() 
{
    std::vector<int> v{ 3, 1, 4 };
 
    auto vi = v.begin();
    std::advance(vi, 2);
    std::cout << *vi << ' ';
 
    vi = v.end();
    std::advance(vi, -2);
    std::cout << *vi << '\n';
}
```
Output:  
``` cmd
4 1
```

## std::prev
### 参数
- **`it`** :	迭代器
- **`n`**   :	it 要被减少的次数

### 返回值
返回迭代器 it 的第 n 个前驱。 

### 复杂度
线性。  
然而，若 BidirIt 还满足遗留随机访问迭代器 (LegacyRandomAccessIterator) 的要求，则复杂度为常数。

### 示例
Code:  
```C++
#include <iostream>
#include <iterator>
#include <vector>
 
int main() 
{
    std::vector<int> v{ 3, 1, 4 };
 
    auto it = v.end();
    auto pv = std::prev(it, 2);
    std::cout << *pv << '\n';
 
    it = v.begin();
    pv = std::prev(it, -2);
    std::cout << *pv << '\n';
}
```
Output:  
``` cmd
1
4
```

## std::next
### 参数
- **`it`** :	迭代器
- **`n`**   :	要前进的元素数

### 返回值
迭代器 it 的第 n 个后继。

### 复杂度
线性。  
然而，若 InputIt 还满足遗留随机访问迭代器 (LegacyRandomAccessIterator) 的要求，则复杂度为常数。

### 示例
Code:  
```C++
#include <iostream>
#include <iterator>
#include <vector>
 
int main() 
{
    std::vector<int> v{ 4, 5, 6 };
 
    auto it = v.begin();
    auto nx = std::next(it, 2);
    std::cout << *it << ' ' << *nx << '\n';
 
    it = v.end();
    nx = std::next(it, -2);
    std::cout << ' ' << *nx << '\n';
}
```
Output:  
``` cmd
4 6
 5
```