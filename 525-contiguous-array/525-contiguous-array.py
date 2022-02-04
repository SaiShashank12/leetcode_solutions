class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
            hash_map={}
            hash_map[0]=-1
            max_len=0
            count=0
            for i in range(len(nums)):
                count+=1 if nums[i]==1 else -1
                if count in hash_map:
                    max_len=max(max_len,i-hash_map.get(count))
                else:
                    hash_map[count]=i
            return max_len
            
            