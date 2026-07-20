class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        s_nums = set(nums)
        if len(s_nums) == len(nums):
            return False
        else:
            return True
