#question:
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#code:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_red = 0 
        count_white = 0 
        count_blue = 0
        for num in nums:
            if num == 0:
                count_red += 1
            elif num == 1:
                count_white += 1
            else:
                count_blue += 1
         
        i = 0
        for red in range(count_red):
            nums[i] = 0
            i += 1
        for white in range(count_white):
            nums[i] = 1
            i += 1
        for blue in range(count_blue):
            nums[i] = 2
            i += 1
        return nums
        