class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenteses_dict = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for i in range(len(s)):
            if s[i] in parenteses_dict.keys():
                stack.append(s[i])
            elif s[i] in parenteses_dict.values():
                if not stack or parenteses_dict[stack.pop()] != s[i]:
                    return False
        return not stack