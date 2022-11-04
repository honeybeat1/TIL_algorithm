class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                mid = left + 1
            else:
                mid = right
        if mid[left] < target:
            return left + 1
        else:
            return left
