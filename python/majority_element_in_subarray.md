Implementing the class MajorityChecker, which has the following API:

    MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
    int query(int left, int right, int threshold) has arguments such that:
        0 <= left <= right < arr.length representing a subarray of arr;
        2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray

Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

 

Example:

```
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
``` 

Constraints:

    1 <= arr.length <= 20000
    1 <= arr[i] <= 20000
    For each query, 0 <= left <= right < len(arr)
    For each query, 2 * threshold > right - left + 1
    The number of queries is at most 10000

Code:

```python
class MajorityChecker:
    def __init__(self, arr: List[int]):
        # create a dictionary of numbers and their index locations
        num_locations = defaultdict(list)
        for i, num in enumerate(arr):
            num_locations[num].append(i)

        # sort the dictionary items by index location list length
        # presumably to get to the largest repeated number ASAP
        self.occur = sorted(num_locations.items(), reverse=True, key=lambda x: len(x[1]))
        print(f"NUM_LOCATIONS:\n{num_locations}")
        print(f"SELF.OCCUR:\n{self.occur}")

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, locations in self.occur:
        
            # return immediately if threshold isn't met by largest repeat
            if len(locations) < threshold:
                return -1

            # i and j are virtual markers that expose how many
            # repeats of a specific number occur when i is subtracted from j
            i = bisect.bisect_left(locations, left)
            j = bisect.bisect_right(locations, right)
            print(f"QUERY: ({left}, {right}, {threshold})")
            print(f"BISECT_LEFT: {i}, BISECT_RIGHT: {j}")

            # if repeats (defined by j - i) meet or exceed threshold
            # return current number
            if j - i >= threshold:
                return num
        return -1
```
