#question
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#code:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = []
        b = []
        for i in nums:
            if i in a:
                b.append(i)
            else:
                a.append(i)
        for j in b:
            if j in a:
                a.remove(j)
        for z in a:
            return z


