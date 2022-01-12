
class Solution:
    def helper(self, s, t):
        i, j =0 ,0
        if(len(t) > len(s)):
            return False
        while(i <len(s) and j <len(t)):
            if(s[i] != t[j]):
                print(f"not equal {i} : {j}")
                return False
            m = i+1
            while(m < len(s) and s[m-1] == s[m]):
                m+=1
            counta = m -i
            n = j+1
            while(n <len(t) and t[n-1] == t[n]):
                n+=1
            countb = n-j
          
            if(countb > counta)           :
                return False
            if(counta != countb and counta < 3):
                print(f"a : {counta} b :{countb}  ")
                return False
            i = m
            j = n
        
        return False if i<len(s) or j < len(t) else True    
            
                
    def expressiveWords(self, s: str, words: List[str]) -> int:
       
        count = 0
        for word in words:
            
            print(f"  {word}   ")
            status = self.helper(s, word)
          
            if(status):
                count += 1
           
        print(f"count is {count}")
        return count