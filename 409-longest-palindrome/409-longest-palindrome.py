class Solution:
    def longestPalindrome(self, s: str) -> int:
        values = sorted(list(collections.Counter(s).values()),reverse=True)
        
        count = 0
        odd_val = False
        for idx,val in enumerate(values):
            if val % 2 ==0: # count all values with even occurences
                count += val
            else:
                count += val-1      #count highest odd value minus 1.
                if not odd_val:     #if first i.e. highest odd value 
                    count +=1       # add one 
                    odd_val = True  # ignore all other odd values
                
        return count