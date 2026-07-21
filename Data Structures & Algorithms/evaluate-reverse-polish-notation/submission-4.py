class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for txt in tokens:
            if txt not in "+-*/":
                txt = int(txt)
                stack.append(txt)
            else:
                match txt:
                    case '+':
                        b = stack.pop()
                        a = stack.pop()
                        res = a + b
                        stack.append(res)
                    case '-':
                            b = stack.pop()
                            a = stack.pop()
                            res = a - b
                            stack.append(res)
                    case '*':
                            b = stack.pop()
                            a = stack.pop()
                            res = a * b
                            stack.append(res)
                    case '/':
                            b = stack.pop()
                            a = stack.pop()
                            res = int(a / b)
                            # a/b -> 실수 형태
                            # a//b -> 0 아닌 무한대로 내림
                            # int(a/b) -> 0 방향으로 소수점 버려짐
                            stack.append(res)
        return stack.pop()            