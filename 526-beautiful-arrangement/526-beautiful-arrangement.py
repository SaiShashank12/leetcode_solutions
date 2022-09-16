class Solution:
    def countArrangement(self, n: int) -> int:
        self.visited=[False]*(n+1)
        self.count=0
        
        def calculate(pos,n):
            if pos>n:self.count+=1
            for i in range(1,n+1):
                if not self.visited[i] and (pos%i==0 or i%pos==0):
                    self.visited[i]=True
                    calculate(pos+1,n)
                    self.visited[i]=False
        
        calculate(1,n)
        return self.count