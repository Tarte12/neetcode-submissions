class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(0, n-1): #인덱스 0부터 n-1까지 nums[0] ~ nums[n-1]
            for j in range(1+i, n): #인덱스 1부터 n까지 nums[1] ~ nums[n]
                if nums[i] + nums[j] == target:
                    return [i, j]
            
                