class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        i=0
        while i <len(s):
            
            while i<len(s) and s[i]=='#':
                if not stack1 :
                    i+=1
                    continue
                stack1.pop()
                i+=1
            
            else:
                if i<len(s):
                    stack1.append(s[i])
            i+=1
        stack2=[]
        i=0
        while i <len(t):
            
            while i<len(t) and t[i]=='#':
                if not stack2 :
                    i+=1
                    continue
                stack2.pop()
                i+=1
            else:
                if i<len(t):
                    stack2.append(t[i])
            i+=1
        
        return stack1==stack2
        
                