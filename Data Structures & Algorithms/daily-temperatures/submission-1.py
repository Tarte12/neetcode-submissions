class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 더 따뜻한 날씨가 올 때까지 stack에 쌓고 len이 며칠인지 알려줄 듯
        # 근데 요소별로 알아야 하니까 for문 돌리면서 안에서 stack 초기화 필요
        n = len(temperatures)
        answer = [0]*n
        stack = []
        for i in range(n):
            # 스택에 과거 날짜가 들어 있고
            # 오늘(i) 온도가 과거 날짜 온도보다 높다면 반복
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_i = stack.pop()
                answer[prev_i] = i - prev_i
            
            # 오늘 날짜(i)는 다음 날들과 비교하기 위해 스택 쌓기
            stack.append(i)

        return answer
