class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        stack=[start]
        actions=[(0,-1),(0,+1),(-1,0),(+1,0)]
        m,n=len(maze),len(maze[0])
        while stack:
            curr_row,curr_col=stack.pop()
            maze[curr_row][curr_col]=-1
            for i in actions:
                new_row,new_col=curr_row,curr_col
                while 0<=new_row+i[0]<m and 0<=new_col+i[1]<n and maze[new_row+i[0]][new_col+i[1]]!=1:
                    new_row+=i[0]
                    new_col+=i[1]
                if [new_row,new_col]==destination:
                    return True
                if maze[new_row][new_col]!=-1:
                    maze[new_row][new_col]=-1
                    stack.append([new_row,new_col])
        return False