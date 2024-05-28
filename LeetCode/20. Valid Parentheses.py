  '''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
'''

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack :
                    return False
                last = stack.pop()
                if last == '(' and char != ')':
                    return False
                if last == '[' and char != ']':
                    return False
                if last == '{' and char != '}':
                    return False
        if stack:
            return False
        return True


#testing
result = Solution().isValid(s="[(][]{}")
print(result)
