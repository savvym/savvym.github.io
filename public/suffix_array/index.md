# [算法刷题]后缀数组Suffix Array


## 后缀数组概念
设有一字符串`s` 
1. 子串
   字符串`s`的子串为`s`中从下标`i`到下标`j`的连续的一段字符组成的字符串`s[i...j]`，假设字符串下标从`1`开始.
2. 后缀
   指从某个位置`i`开始到整个字符串末尾的一个子串，记作`suffix(i) = s[i...len(s)]`.
3. 字符串大小比较
   按字典顺序比较，显然两个不同开头位置的后缀`suffix(i)`和`suffix(j)`不可能相等，即`suffix(i) != suffix(j) (i != j)`
4. 后缀数组
   `sa`为一个一维数组，保存了`1~n`的某个排列`sa[1]、sa[2]、... sa[n]`，满足`suffix(sa[i]) < suffix(sa[i + 1])`
5. 名次数组
   `rank`为一个名次数组，其中`rank[i]`为`suffix(i)`在所有后缀中从小到大的名次为多少。  

**总的来说就是，后缀数组`sa`记录了排第几的是哪个后缀，名次数组`rank`记录了当前这个后缀排第几。**

例子：  
```c++
设字符串s = aabaaaab

suffix(1) = aabaaaab
suffix(2) = abaaaab
suffix(3) = baaaab
suffix(4) = aaaab
suffix(5) = aaab
suffix(6) = aab
suffix(7) = ab
suffix(8) = b

最小的后缀应该是suffix(4)，然后是suffix(5) ...
得到以下后缀数组
sa[1] = 4 // aaaab
sa[2] = 5 // aaab 
sa[3] = 6 // aab
sa[4] = 1 // aabaaaab
sa[5] = 7 // ab
sa[6] = 2 // abaaaab
sa[7] = 8 // b
sa[8] = 3 // baaaab
由此也能得到名次数组
rank|4|6|8|1|2|3|5|7|
---------------------
s   |a|a|b|a|a|a|a|b|
```
> 设字符串长度为`n`。为了方便比较大小，可以在字符串后面添加一个字符，这个字符没有在前面的字符出现过，而且比前面的字符都要小。在求出名次数组后，可以仅用`O(1)`的时间比较任意两个后缀的大小。在求出后缀数组或者名次数组其中的一个，可以在`O(n)`的时间求出另外一个。

## 构造后缀数组
### 倍增算法 O(NlogN)
```CPP
// 后缀数组，生成sa，rk，height数组
template<class T=string,int range=128>
struct SuffixArray{
    T s;
    int n,bucketRange;
    int sa[range],second[range],bucket[range],mem[range],rk_mem[range+1],rk2_mem[range+1],height[range],*rk,*rk2;
    SuffixArray(const T&_s):s(_s),n(s.size()),bucketRange(range){
        rk=rk_mem;
        rk2=rk2_mem;
        rk[n]=rk2[n]=-1;
        memset(bucket,0,sizeof(bucket));
        for(int i=0;i<n;i++)bucket[rk[i]=s[i]]++;
        for(int i=1;i<bucketRange;i++)bucket[i]+=bucket[i-1];
        for(int i=0;i<n;i++)sa[--bucket[rk[i]]]=i;
        for(int w=1;;w<<=1){
            int j=0;
            for(int i=n-w;i<n;i++)second[j++]=i;
            for(int i=0;i<n;i++)if(sa[i]>=w)second[j++]=sa[i]-w;
            memset(bucket,0,sizeof(bucket));
            for(int i=0;i<n;i++)bucket[mem[i]=rk[second[i]]]++;
            for(int i=1;i<bucketRange;i++)bucket[i]+=bucket[i-1];
            for(int i=n-1;i>=0;i--)sa[--bucket[mem[i]]]=second[i];
            bucketRange=0;
            for(int i=0;i<n;i++){
                rk2[sa[i]]=!i||(rk[sa[i]]==rk[sa[i-1]]&&rk[sa[i]+w]==rk[sa[i-1]+w])?bucketRange:++bucketRange;
            }
            swap(rk,rk2);
            if(++bucketRange==n)break;
        }
    }
    void getHeight(){
        memset(height,0xff,sizeof(height));
        for(int i=0,h=0;i<n;i++){
            if(h)h--;
            if(rk[i])while(sa[rk[i]-1]+h<n&&s[i+h]==s[sa[rk[i]-1]+h])h++;
            height[rk[i]]=h;
        }
    }
};

```
### 3DC算法 O(N)
``` CPP
// TODO
```
### SA-IS O(N)
模板
```cpp
class SuffixArray {
public:
    using size_type = unsigned;
    using pointer = size_type*;
    using const_pointer = const size_type*;

private:
    template<typename It>
    inline static void get_sbuk(It s, pointer sbuk, size_type n, size_type m) {
        std::fill_n(sbuk, m, 0);
        for (size_type i = 0;i < n;++i)
            ++sbuk[s[i]];
        std::partial_sum(sbuk, sbuk + m, sbuk);
    }

    inline static void lbuk_to_sbuk(const_pointer lbuk, pointer sbuk, size_type n, size_type m) {
        std::copy_n(lbuk + 1, m - 1, sbuk);
        sbuk[m - 1] = n;
    }

    inline static void sbuk_to_lbuk(pointer lbuk, const_pointer sbuk, size_type n, size_type m) {
        std::copy_n(sbuk, m - 1, lbuk + 1);
        lbuk[0] = 0;
    }

    template<bool Stage, typename It>
    inline static void induced_sort(It s, pointer sa, pointer lbuk, pointer sbuk, size_type n, size_type m) {
        constexpr size_type mask = size_type(1) << (CHAR_BIT * sizeof(size_type) - 1);
        using value_type = typename std::iterator_traits<It>::value_type;
        value_type prev = s[n - 1], cur;
        pointer ptr = sa + lbuk[prev];
        *ptr++ = n - 1;
        for (size_type p, i = 0;i < n;++i) {
            if ((p = sa[i] - 1) & mask) continue;
            if ((cur = s[p]) < s[p + 1]) {
                sa[i] = ~p;
                continue;
            }
            if (cur != prev) {
                lbuk[prev] = ptr - sa;
                ptr = sa + lbuk[prev = cur];
            }
            *ptr++ = p;
            if (!Stage) sa[i] = 0;
        }
        ptr = sa + sbuk[prev = 0];
        sbuk_to_lbuk(lbuk, sbuk, n, m);
        for (size_type p, i = n;i-- > 0;) {
            if ((p = ~sa[i]) & mask) continue;
            if ((cur = s[p]) > s[p + 1]) {
                sa[i] = p + 1;
                continue;
            }
            if (cur != prev) {
                sbuk[prev] = ptr - sa;
                ptr = sa + sbuk[prev = cur];
            }
            *--ptr = ~p + 1;
            sa[i] = Stage ? p + 1 : 0;
        }
    }

    template<typename It>
    inline static size_type fill_lms_char(It s, pointer sa, pointer mid, pointer sbuk, size_type n) {
        using value_type = typename std::iterator_traits<It>::value_type;
        const pointer len = mid;
        pointer pos = mid;
        value_type prev, cur = s[n - 1];
        for (size_type j = n - 1, i = n - 1;i > 0;) {
            do prev = cur; while (i > 0 && (cur = s[--i]) >= prev);
            if (cur >= prev) break;
            do prev = cur; while (i > 0 && (cur = s[--i]) <= prev);
            if (cur <= prev) break;
            const size_type p = i + 1;
            sa[--sbuk[s[p]]] = p;
            len[p / 2] = j - i;
            *--pos = j = p;
        }
        return mid - pos;
    }

    template<typename It>
    inline static void fill_lms_suffix(It s, pointer sa, const_pointer pos, pointer sbuk, size_type n, size_type m, size_type n0) {
        using value_type = typename std::iterator_traits<It>::value_type;
        value_type prev = m, cur;
        size_type j = n;
        for (size_type p, i = n0;i > 0;) {
            if ((cur = s[p = pos[sa[--i]]]) != prev) {
                const size_type b = sbuk[prev = cur];
                while (j > b) sa[--j] = 0;
            }
            sa[--j] = p;
        }
        while (j > 0) sa[--j] = 0;
    }

    template<typename It>
    inline static size_type rename(It s, pointer sa, const_pointer len, size_type n, size_type m, size_type n0) {
        for (size_type p, j = 0, i = 0;j < n0;++i) {
            if ((p = sa[i]) != 0) {
                sa[i] = 0;
                sa[j++] = p;
            }
        }
        const pointer sa0 = sa, s0 = sa + n0;
        size_type m0 = 0, plen = 0;
        It ppos = s;
        for (size_type i = 0;i < n0;++i) {
            const size_type p = sa[i], nlen = len[p / 2];
            if (nlen != plen || !std::equal(ppos, ppos + plen, s + p)) ++m0;
            s0[p / 2] = m0;
            ppos = s + p;
            plen = nlen;
        }
        for (size_type p, j = 0, i = 0;j < n0;++i)
            if ((p = s0[i]) != 0)
                s0[j++] = p - 1;
        return m0;
    }

public:    
    template<typename It>
    static void suffix_sort(It s, pointer sa, pointer buf, pointer lbuk, pointer sbuk, size_type n, size_type m) {
        static_assert(std::is_same_v<typename std::iterator_traits<It>::iterator_category, std::random_access_iterator_tag>);
        std::fill_n(sa, n, 0);
        get_sbuk(s, sbuk, n, m);
        sbuk_to_lbuk(lbuk, sbuk, n, m);
        const pointer mid = buf + n / 2;
        const size_type n0 = fill_lms_char(s, sa, mid, sbuk, n);
        const pointer len = mid, pos = mid - n0;
        lbuk_to_sbuk(lbuk, sbuk, n, m);
        induced_sort<0>(s, sa, lbuk, sbuk, n, m);
        const size_type m0 = rename(s, sa, len, n, m, n0);
        const pointer sa0 = sa, s0 = sa + n0;
        if (m0 < n0)
            suffix_sort(s0, sa0, mid, sbuk, sbuk + m0, n0, m0);
        else for (size_type i = 0;i < n0;++i)
            sa0[s0[i]] = i;
        lbuk_to_sbuk(lbuk, sbuk, n, m);
        fill_lms_suffix(s, sa, pos, sbuk, n, m, n0);
        induced_sort<1>(s, sa, lbuk, sbuk, n, m);
    }

private:
    std::unique_ptr<size_type[]> data;

public:
    const const_pointer sa, rk, ht;

public:
    template<typename It>
    SuffixArray(It s, size_type n, size_type m)
        : data(new size_type[3 * n]), sa(data.get()), rk(sa + n), ht(rk + n) {
        const pointer sa = data.get(), rk = sa + n, ht = rk + n;
        const unique_ptr<size_type[]> lbuk(new size_type[m]);
        if (m <= n)
            suffix_sort(s, sa, rk, lbuk.get(), ht, n, m);
        else {
            const unique_ptr<size_type[]> sbuk(new size_type[m]);
            suffix_sort(s, sa, rk, lbuk.get(), sbuk.get(), n, m);
        }
        for (size_type i = 0;i < n;++i)
            rk[sa[i]] = i;
        for (size_type k = 0, i = 0;i < n;++i) {
            if (rk[i] == 0) continue;
            if (k > 0) --k;
            const size_type j = sa[rk[i] - 1];
            const size_type l = n - std::max(i, j);
            for (;k < l;++k) if (s[i + k] != s[j + k]) break;
            ht[rk[i]] = k;
        }
    }

    template<typename S>
    SuffixArray(const S& s, size_type m) : SuffixArray(std::data(s), std::size(s), m) {}
};

```
## 后缀数组相关题目
[LeetCode 1923.最长公共子路径](https://leetcode.cn/problems/longest-common-subpath/description/)  
1. 主代码（后缀数组为倍增算法模板）
```cpp 
class Solution {
    //用counter来计数覆盖的path数量
    //为何不用bool数组或者 bitset: 初始化的时间复杂度会超标
    struct{
        int mark[100000]={0},num=0;
        int timestamp=0;
        void reset(){
            timestamp++;
            num=0;
        }
        void add(int i){
            if(mark[i]!=timestamp){
                mark[i]=timestamp;
                num++;
            }
        }
    }counter;
public:
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        int m=paths.size();
        //all存放全部路径，sublen表示每个位置作为开头的最长子串长度，belong表示所属的路
        vector<int>all,sublen,belong;
        for(int i=0;i<m;i++){
            for(int j=0;j<paths[i].size();j++){
                all.push_back(paths[i][j]);
                sublen.push_back(paths[i].size()-j);
                belong.push_back(i);
            }
        }
        //后缀数组结构体自动生成 sa,rk,height 数组
        SuffixArray<vector<int>,100000>SA(all);
        SA.getHeight();
        auto sa=SA.sa,h=SA.height;
        //二分找出最低的height，使某个高于height的区间内包含所有的path
        int low=0,high=all.size();
        while(low<high){
            int mid=(low+high+1)/2;
            bool flag=false;
            for(int i=0,j;i<all.size();i=j){
                counter.reset();
                for(j=i;j<all.size()&&(j==i||h[j]>=mid);j++){
                    if(sublen[sa[j]]>=mid)counter.add(belong[sa[j]]);
                }
                if(counter.num==m){
                    flag=true;
                    break;
                }
            }
            if(flag)low=mid;
            else high=mid-1;
        }
        return low;
    }
};
```
SA-IS模板主代码
```cpp
const int N = 200010;
class Solution {
public:
    int s[N]; // 将串拼接起来,中间用不同字符隔开,结尾改为0
    int belong[N]; // 当前字符属于第几个朋友
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        int len = 0;
        int m = paths.size(); // 朋友数量
        for (int i = 0; i < m; i ++ ) {
            for (int c: paths[i]) {
                s[len] = c + 1; // 从1开始
                belong[len] = i + 1;
                len ++ ;
            }
            s[len ++ ] = 1e5 + 10;
        }
        s[ -- len] = 0;
        SuffixArray sa(s, len + 1, 1e6);
    
        // 找到大于等于答案的每一段height区间[i, j]
        // 如果[i - 1, j]的后缀包含了所有朋友则满足条件
        auto check = [&](int mid) -> bool {
            for (int i = 1; i <= len; i ++ ) {
                if (sa.ht[i] >= mid) {
                    vector<bool> seen(m + 1, false);
                    int j = i + 1;
                    while (j <= len && sa.ht[j] >= mid) j ++ ;
                    j -- ;
                    int c = 0;
                    for (int k = i - 1; k <= j; k ++ ) {
                        if (seen[belong[sa.sa[k]]]) continue;
                        c ++ ;
                        seen[belong[sa.sa[k]]] = true;
                    }
                    if (c == m) return true;
                    i = j + 1;
                }
            }
            return false;
        };

        // 二分答案
        int l = 0, r = len;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (!check(mid + 1)) r = mid;
            else l = mid + 1;
        }
        return l;
    }
};
```


