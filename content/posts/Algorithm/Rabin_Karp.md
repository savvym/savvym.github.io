---
title: "[算法刷题]滚动哈希Rabin-Karp算法"
date: 2023-04-15
summary: "滚动哈希及其应用"
categories:
- Algorithm
tags:
- C++
- Algorithm
---
[1147.段氏回文](https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/description/)  
你会得到一个字符串`text` 。你应该把它分成`k`个子字符串`(subtext1, subtext2，…， subtextk)`，要求满足:  
- `subtexti`是**非空**字符串
- 所有子字符串的连接等于`text`(即`subtext1 + subtext2 + ... + subtextk == text`)
- 对于所有`i`的有效值(即`1 <= i <= k`) ,`subtexti == subtextk - i + 1`均成立

返回k可能的最大值

示例1:
```
输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
```
示例2:
```
输入：text = "merchant"
输出：1
解释：我们可以把字符串拆分成 "(merchant)"。
```
示例3:
```
输入：text = "antaprezatepzapreanta"
输出：11
解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。
```

滚动哈希解法：

```c++
using ll = long long;

class Solution {
public:
    vector<ll> pre1, pre2;
    vector<ll> pow1, pow2;
    int base1, base2;
    static constexpr int MOD1 = 1e9 + 7;
    static constexpr int MOD2 = 1e9 + 9;

    void init(string& s) {
        std::mt19937 gen{random_device{}()};
        base1 = uniform_int_distribution<int>(1e6, 1e7)(gen);
        base2 = uniform_int_distribution<int>(1e6, 1e7)(gen);
        while (base2 == base1) {
            base2 = uniform_int_distribution<int>(1e6, 1e7)(gen);
        }
        int n = s.size();
        pre1.resize(n + 1);
        pre2.resize(n + 1);
        pow1.resize(n);
        pow2.resize(n);
        pow1[0] = pow2[0] = 1;
        pre1[1] = pre2[1] = s[0];
        for (int i = 1; i < n; i++) {
            pre1[i + 1] = (pre1[i] * base1 + s[i]) % MOD1;
            pre2[i + 1] = (pre2[i] * base2 + s[i]) % MOD2;
            pow1[i] = (pow1[i - 1] * base1) % MOD1;
            pow2[i] = (pow2[i - 1] * base2) % MOD2;
        }
    }

    pair<int, int> getHash(int l, int r) {
        return {(pre1[r + 1] - ((pre1[l] * pow1[r - l + 1]) % MOD1) + MOD1) % MOD1, (pre2[r + 1] - (pre2[l] * pow2[r - l + 1]) % MOD2 + MOD2) % MOD2};
    }
    int longestDecomposition(string text) {
        init(text);
        int n = text.size();
        int res = 0;
        int l = 0, r = n -1;
        while (l <= r) {
            int len = 1;
            while (l + len - 1 < r - len + 1) {
                if (getHash(l, l + len - 1) == getHash(r - len + 1, r)) {
                    res += 2;
                    break;
                }
                len++;
            }
            if (l + len - 1 >= r - len + 1) {
                res++;
            }
            l += len;
            r -= len;
        }
        return res;
    }
};
```