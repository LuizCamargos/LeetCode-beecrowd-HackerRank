'''
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word=ransomNote
        for letter in ransomNote:
            if letter in magazine:
                word=word.replace(letter, "", 1)
                magazine=magazine.replace(letter, "", 1)
            else:
                word="-"
                break

        return word==""

#testing
result = Solution().canConstruct(ransomNote = "aa", magazine = "aab")
print(result)
