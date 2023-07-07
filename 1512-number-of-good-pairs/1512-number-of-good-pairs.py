class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        size = len(nums)
        
        for i in range(size - 1):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    sum += 1
                
        return sum