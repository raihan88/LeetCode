class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        temp = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            if nums[i] == total - 2*temp:
                return i
            temp += nums[i]
        return -1
            