class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum_= nums[l]+nums[r]+nums[i]
                if sum_>0:
                    r-=1
                elif sum_<0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1   
        print(res)        
        res_ = [list(t) for t in set(map(tuple,res))]
        return (res_)