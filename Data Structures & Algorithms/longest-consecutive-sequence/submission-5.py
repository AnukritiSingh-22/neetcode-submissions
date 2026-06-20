class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        res = defaultdict(set)
        for i in sorted(nums):
            if i in res.values():
                continue
            j=i
            while j in nums:
                res[i].add(j)
                j+=1
        print(res.items())
        lis = [len(i) for i in res.values()]
        return max(lis)