class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        
#     Algorithm:
        
#             Summary: We are going to have 2 dp arrays pos and neg.
#             The element at index i of dp array pos indicates the maximum length positive subarray
#             ending at that point and an element at index i of the negative subarray indicates the
#             maximum length negative subarray ending at that point.

#             Steps:
        
#          1) We will check the fist element and if positive we will make pos[0] = 1
#             else neg[0] = 1
            
#          2) Start iterating from the 1st element. Now at each index the element at position i 
#             in nums array can be positive, negative or 0.
            
#          3) If nums[i] is positive, then the max positive product ending at that point would be 
#             pos[i-1] + 1, since pos[i] stores the maximum positive product stored till previous        #             index.
        
#             The max negative product neg[i] till that point would be neg[i-1] + 1 if neg[i-1]>0. This               is because only if neg[i-1]>0, we have a negative product ending at the previous index # #             and there is a possible way to make the current product negative, else neg[i]=0
            
#           4) if nums[i] is negative, then the neg[i] = pos[i-1] + 1
#              and pos[i] will be neg[i-1] +  1 , if neg[i-1]>0.
            
#           5) if nums[i] is 0, then there is no positive or negative product ending at i, hence both                  pos[i] and neg[i] will be 0.
        
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        
        if nums[0] > 0 :
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
            
        max_tracker = pos[0]
        
        for i in range(1,len(nums)):
            
            if nums[i] < 0:
                if neg[i-1]>0:
                    pos[i] = neg[i-1] + 1
                else:
                    pos[i] = 0
                
                neg[i] = pos[i-1] + 1

                
            elif nums[i] > 0:
                
                pos[i] = pos[i-1] + 1
                if neg[i-1]>0:
                    neg[i] = neg[i-1] + 1
                else:
                    neg[i] = 0
                    
 
                
            else:
                pos[i] = 0
                neg[i] = 0

            max_tracker = max(max_tracker, pos[i])
            
        return max_tracker
 