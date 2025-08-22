#qn
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#code
class Solution:
    def rob(self, nums: List[int]) -> int:
            n = len(nums)
            if n == 1:
                return nums[0]
            prev1, prev2 = 0, 0
            for i in range(n-1):  
                prev1, prev2 = max(prev2 + nums[i], prev1), prev1
            case1 = prev1
            prev1, prev2 = 0, 0
            for i in range(1, n): 
                prev1, prev2 = max(prev2 + nums[i], prev1), prev1
            case2 = prev1
