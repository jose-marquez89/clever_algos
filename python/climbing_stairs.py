"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class TheirSolution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if n==1:
            return f1
        if n==2:
            return f2
        #f=0
        for i in range(2,n):
            f= f1 + f2
            f1 = f2
            f2 = f
        return f 
      
      
 # My solution (requires import math)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        
        output = 1 
        
        repeat = n // 2
        starting_point = (n - 2) + 1
        
        for i in range(repeat):
            N = starting_point
            K = i+1
            denom = math.factorial(N - K) * math.factorial(K)
            combos = math.factorial(N) / denom
            output += combos
            starting_point -= 1
            
        return int(output)
