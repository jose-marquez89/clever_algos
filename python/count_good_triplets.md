# Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

```    
       0 <= i < j < k < arr.length
       |arr[i] - arr[j]| <= a
       |arr[j] - arr[k]| <= b
       |arr[i] - arr[k]| <= c
```

Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

```
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
```

Example 2:

```
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
```
 

Constraints:

```
    3 <= arr.length <= 100
    0 <= arr[i] <= 1000
    0 <= a, b, c <= 1000
```


### Clever solution
This is not my solution, found this on Leetcode.com, i'll add my solution (much slower) below it.

```python3
import sortedcontainers


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        right = sortedcontainers.SortedList(arr)
        left = sortedcontainers.SortedList()

        res = 0
        for n in arr:
            right.remove(n)

            r_start, r_end = right.bisect_left(n - b), right.bisect_right(n + b)
            l_start, l_end = left.bisect_left(n - a), left.bisect_right(n + a)

            l2 = left[l_start:l_end]

            for v in right[r_start:r_end]:
                res += bisect.bisect_right(l2, v + c) - bisect.bisect_left(l2, v - c)

            left.add(n)

        return res
```

My significantly slower solution:
```python3
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        i = 0
        j = i + 1
        k = i + 2
        
        while i <= len(arr) - 3:
            good_triplet = True
            if abs(arr[i] - arr[j]) > a:
                good_triplet = False
            if abs(arr[j] - arr[k]) > b:
                good_triplet = False
            if abs(arr[i] - arr[k]) > c:
                good_triplet = False
            
            if k == len(arr) - 1 and j == len(arr) - 2:
                i += 1
                j = i + 1
                k = i + 2
            elif k == len(arr) - 1:
                j += 1
                k = j + 1
            else:
                k += 1
            
            if good_triplet:
                count += 1
                
        return count
 ```
