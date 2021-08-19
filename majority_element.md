Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -231 <= nums[i] <= 231 - 1

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

My Solution(s):
```javascript
var majorityElement = function(nums) {
    /* solution 1
    let counts = {};
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in counts) {
            counts[nums[i]]++;
        } else {
            counts[nums[i]] = 1;
        }
    }
    
    let countsZipped = Object.keys(counts).map(x => [x, counts[x]]);
    let countsSorted = countsZipped.sort((x, y) => x[1] < y[1] ? 1 : -1) 
    
    return countsSorted[0][0];
    */
    
    // solution 2
    let numsSorted = nums.sort();
    let majority = highest = curCount = 0;
    let curNum = numsSorted[0];
    
    for (let i = 0; i < numsSorted.length; i++) {
       if (numsSorted[i] != curNum) {
           if (curCount > highest) {
               majority = curNum;
               highest = curCount;
           }
           curNum = numsSorted[i];
           curCount = 1;
       } else {
           curCount++;
       } 
    }
    
    if (curCount > highest) {
        majority = numsSorted[numsSorted.length-1];
    }
    
    return majority;
    
};
```

Clever algo:
```javascript
const majorityElement = (nums) => {
    let maj = 0;
    let count = 1;
    for(let i = 1; i < nums.length; i++) {
        nums[i] === nums[maj] ? count++ : count--;
    if(count === 0) {
        maj = i;
        count++;
    }    
    }
    return nums[maj];
    }
```
