class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char in mapping:
                stack.append(char)
            else: 
                if not stack or mapping[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0
        