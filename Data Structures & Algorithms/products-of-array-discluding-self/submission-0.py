class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n):
                res = 1
                for j in range(n):
                    if i != j:
                        res *= nums[j]
                answer.append(res)
        return answer
            
        