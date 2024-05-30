'''
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

from typing import List

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter=0
        while num!=0:
            if num%2==0:
                num/=2
            else:
                num-=1
            counter+=1
        return counter

#testing
result = Solution().numberOfSteps(num = 123)
print(result)
