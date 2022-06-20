---
title: "C++ STL advance(), prev() and next()"
date: 2022-06-20
summary: "C++ STL advance, prev() and next()"
categories:
- C++
tags:
- C++
- STL
# hidemeta: true
---
> Defined in header `<iterator>`

## std::advance

Increments given iterator it by n elements.  
If n is negative, the iterator is decremented. In this case, InputIt must meet the requirements of *LegacyBidirectionalIterator*, otherwise the behavior is undefined.

### Parameters
- **`it`** :	iterator to be advanced
- **`n`**   :	number of elements it should be advanced

### Return value
(none)

### Complexity
Linear.  
However, if InputIt additionally meets the requirements of *LegacyRandomAccessIterator*, complexity is constant.

### Example
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
### Parameters
- **`it`** :	an iterator
- **`n`**   :	number of elements it should be descended

### Return value
The nth predecessor of iterator it.

### Complexity
Linear.  
However, if InputIt additionally meets the requirements of *LegacyRandomAccessIterator*, complexity is constant.

### Example
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
### Parameters
- **`it`** :	an iterator
- **`n`**   :	number of elements to advance

### Return value
The nth successor of iterator it.

### Complexity
Linear.  
However, if InputIt additionally meets the requirements of *LegacyRandomAccessIterator*, complexity is constant.

### Example
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