Given a string s, find the length of the longest substring without repeating characters.

 
```
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
```
 

Constraints:
```
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
```

My solution:
```python
# this was very slow
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        if s == "":
            return 0
        
        longest = 0
        cur_len = 0
        start = 0
        pos = 0
        prev = []
        
        while pos < len(s):
            if pos > 0 and s[pos] == s[pos-1]: 
                if cur_len > longest:
                    longest = cur_len
                cur_len = 1
                prev = [s[pos]]
                pos += 1
                
            elif s[pos] not in prev:
                prev.append(s[pos])
                cur_len += 1
                pos += 1
            else:
                start = start + prev.index(s[pos]) + 1 
                pos = start
                if cur_len > longest:
                    longest = cur_len
                cur_len = 0  
                prev = []
        
        if cur_len > longest:
            longest = cur_len
        
        return longest
```

Clever algo:
```python
# Clever algo but they used python keywords as variables
# Still a good algo
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = -1
        max = 0
        dict = {}
        
        for i in range(len(s)):
            
            if s[i] in dict and dict[s[i]] > start:
                start = dict[s[i]]
                dict[s[i]] = i
                
            else:
                dict[s[i]] = i
                if i - start > max:
                    max = i - start
        return max
```
