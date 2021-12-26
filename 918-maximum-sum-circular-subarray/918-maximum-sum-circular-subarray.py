

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadaneAlgo(nums):
            #only when caculate min sum will get the empty arr, so return -inf
            if len(nums) == 0:
                return float("-inf");
            best = max(nums);
            prev = 0; # if set as float('-inf') then there is posibility to have number overflow
            
            for i in nums:
                prev = i + max(0,prev);
                best = max(prev,best);
            
            return best;
        
        
        #get the non-circular arrar max subarray:
        res1 = kadaneAlgo(nums);
        
        #get the minium arrary between head and last element
        negNums = [-nums[x] for x in range(1,len(nums)-1)];
        minSubArrary = -kadaneAlgo(negNums);
        numsSum = sum(nums);
        res2 = numsSum - minSubArrary;
        
        return max(res1,res2);