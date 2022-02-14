class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0

        right=left=0
        while right<len(data):
            cnt_one+=data[right]
            right+=1
            
            if right-left>ones:
                cnt_one-=data[left]
                left+=1
            max_one=max(max_one,cnt_one)
        return ones-max_one