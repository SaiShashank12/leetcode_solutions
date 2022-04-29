class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def binary_search(nums,target):
            left, right=0,len(nums)-1
            last=len(nums)
            while left<=right:
                mid=(left+right)//2
                
                if nums[mid]==target and last>mid:
                    last=mid
                    
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
                    
            return last
        def binary_search_(nums,target):
            left, right=0,len(nums)-1
            last=0
            while left<=right:
                mid=(left+right)//2
                
                if nums[mid]==target and last<mid:
                    last=mid
                    
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
                    
            return last
         
    
         
        return len(nums)//2<(binary_search_(nums,target)-binary_search(nums,target))+1