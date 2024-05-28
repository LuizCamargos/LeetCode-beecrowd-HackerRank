'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

'''

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            string=""
            if i%3==0:
                string+="Fizz"
            if i%5==0:
                string+="Buzz"
            if string=="":
                string+=str(i)
            result.append(string)
        return result

#testing
result = Solution().fizzBuzz(n=15)
print(result)
