from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        # 1. 먼저 빈도를 카운트한다
        counts = Counter(nums)
        # 2. 카운트한 빈도를 sort한다
        top_k = counts.most_common(k)
        # most_common(): Counter가 제공하는 빈도수
        # 높은 상위 k개의 (숫자, 빈도수) 튜플 쌍 반환 메서드
        for num, count in top_k:
            answer.append(num)
        return answer
        