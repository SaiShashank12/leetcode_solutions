class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return 0 if nums[0]>nums[1] else 1 
        while (left<=right):
            mid=(left+right)//2
            if (mid+1>=len(nums) and nums[mid]>nums[mid-1]) or (mid-1<0 and nums[mid]>nums[mid+1] ) or (nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]):
                return mid
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
            