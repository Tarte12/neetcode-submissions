class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for txt in s:
            if txt == '(' or txt == '[' or txt == '{':
                stack.append(txt)
            elif not stack:
                return False
            elif txt == ')':
                if stack[-1] == "(":
                    stack.pop()
                else: 
                    return False
            elif txt == ']':
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif txt == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
        