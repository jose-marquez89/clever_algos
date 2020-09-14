class MajorityChecker:
    
    def __init__(self, arr: List[int]):
        num_locations = defaultdict(list)
        for i, num in enumerate(arr):
            num_locations[num].append(i)
        self.occur = sorted(num_locations.items(), reverse=True, key=lambda x: len(x[1]))
        print(f"NUM_LOCATIONS:\n{num_locations}")
        print(f"SELF.OCCUR:\n{self.occur}")

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, locations in self.occur:
            if len(locations) < threshold:
                return -1
            i = bisect.bisect_left(locations, left)
            j = bisect.bisect_right(locations, right)
            print(f"QUERY: ({left}, {right}, {threshold})")
            print(f"BISECT_LEFT: {i}, BISECT_RIGHT: {j}")
            if j - i >= threshold:
                return num
        return -1
