class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_res = 0
        for num in num_set:
            #수열의 시작점
            if (num-1) not in num_set:
                current_num = num
                res = 1
            # 연속된 숫자가 있으면 길이 계속 늘림
                while (current_num+1) in num_set:
                    current_num += 1
                    res += 1
                max_res = max(max_res, res)
        return max_res