from collections import deque
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree,vis, queue, dp = [0]*n, [False]*n, deque([]), [0]*n
        for person in range(n): indegree[favorite[person]]+=1
        for person in range(n):
            if not indegree[person]:
                vis[person]=True
                queue.append(person)
        while queue:
            person = queue.popleft()
            fav = favorite[person]
            dp[fav], indegree[fav] = max(dp[fav],dp[person]+1), indegree[fav]-1
            if not indegree[fav]:
                vis[fav]=True
                queue.append(fav)
        type1,type2 = 0,0
        for person in range(n):
            if not vis[person]:
                cur,length = person,0
                while not vis[cur]: vis[cur], cur, length = True, favorite[cur], length+1
                if length==2: type1+= (dp[person]+dp[favorite[person]]+2) 
                else: type2= max(type2,length)
        return max(type1,type2)