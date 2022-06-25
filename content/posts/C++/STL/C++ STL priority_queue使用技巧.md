---
title: "C++ STL priority_queue使用技巧"
date: 2022-06-25
summary: "C++ STL priority_queue使用技巧"
categories:
- C++
tags:
- C++
- STL
---

## 简介

定义在头文件`<queue>`中

`priority_queue<Type, Container, Functional>`

> ```c++
> template<
>     class T,
>     class Container = std::vector<T>,
>     class Compare = std::less<typename Container::value_type>
> > class priority_queue;
> ```

常用操作：

- `top()`

- `empty()`

- `size()`

- `push()`

- `emplace()`

- `pop()`

## 大、小根堆

对于单一数值类型如`int`类型：

```C++
#include <functional> // 因为用到了greater<int>和less<int>
#include <queue>

// 小顶堆
priority_queue<int, vector<int>, greater<int>> q;
// 大顶堆
priority_queue<int, vector<int>, less<int>> q;
// 默认大顶堆
priority_queue<int> q;
```

对于自定义类型，需要指明容器，以及优先级规则，如`pair<int, int>`类别

```c++
typedef pair<int, int> PII;
priority_queue<PII, vector<PII>, decltype(&cmp)> q(cmp); // cmp为一个比较函数
```

Example code:

```C++
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

// 假设按照pair的第二个数来进行排序，这样说明是按第二个数升序，是小根堆，没啥好说的，记住就行了。
bool cmp(const PII& p1, const PII& p2) {
	return p1.second > p2.second;
}

int main() {
    vector<PII> pairs = {{1, 4}, {2, 9}, {5, 3}, {4, 1}, {3, 6}};
	priority_queue<PII, vector<PII>, decltype(&cmp)> q(cmp); // 声明了一个pair的根据第二个数比较的小根堆
    for (auto p : pairs) {
        q.push(p);
    }
    while (q.size()) {
        cout << q.top().first << q.top().second << endl;
    }
    return 0;
}
```

output:

```C++
4 1
5 3
1 4
3 6
2 9
```

## 综合案例

```C++
#include <functional>
#include <queue>
#include <vector>
#include <iostream>
 
template<typename T>
void print_queue(T q) { // NB: pass by value so the print uses a copy
    while(!q.empty()) {
        std::cout << q.top() << ' ';
        q.pop();
    }
    std::cout << '\n';
}
 
int main() {
    const auto data = {1,8,5,6,3,4,0,9,7,2};
    
    // 默认的是大根堆
 	// 输出结果: 9 8 7 6 5 4 3 2 1 0
    std::priority_queue<int> q;
    
    for(int n : data)
        q.push(n);
 
    print_queue(q);
 
    // 声明了一个小根堆
    // 输出结果：0 1 2 3 4 5 6 7 8 9 
    std::priority_queue<int, std::vector<int>, std::greater<int>>
        q2(data.begin(), data.end());
 
    print_queue(q2);
 
    // 利用lambda表达式来写比较函数
    // 按给定规则，小于号说明是个大根堆，根据两个数与1异或之后的大小。
    auto cmp = [](int left, int right) { return (left ^ 1) < (right ^ 1); };
    std::priority_queue<int, std::vector<int>, decltype(cmp)> q3(cmp);
 
    for(int n : data)
        q3.push(n);
 
    print_queue(q3);
}
```

output:

```C++
9 8 7 6 5 4 3 2 1 0 
0 1 2 3 4 5 6 7 8 9 
8 9 6 7 4 5 2 3 0 1
```



## 总结

1. 默认是大根堆，大的数在顶上

2. `greater<int>`是小根堆，`less<int>`是大根堆。

   ```C++
   // greater:
   constexpr bool operator()(const T &lhs, const T &rhs) const 
   {
       return lhs > rhs; // assumes that the implementation uses a flat address space
   }
   // less:
   constexpr bool operator()(const T &lhs, const T &rhs) const 
   {
       return lhs < rhs; // assumes that the implementation uses a flat address space
   }
   ```

3. 自定义比较函数

   ```C++
   // 小根堆
   bool cmp(const T& t1, const T& t2) {
   	t1 > t2;
   }
   
   // 大根堆
   bool cmp(const T& t1, const T& t2) {
       t1 < t2;
   }
   ```

4. 自定义比较函数写法`priority_queue<T, vector<T>, decltype(&cmp)> q(cmp);`