class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        buckets = buckets = [[] for _ in range(len(nums) + 1)]
        for elem, count in counter.items():
            buckets[count].append(elem)
    
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for elem in buckets[i]:
                res.append(elem)
                if len(res) == k:
                    return res



