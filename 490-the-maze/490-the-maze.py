class Solution:
    # Approach 1: DFS - Iterative
    def hasPath(self,maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        nr, nc = len(maze), len(maze[0])
        actions = [(-1,0), (+1,0), (0,-1), (0,+1)]
        stack = [start]
        while stack:
            cur_row, cur_col = stack.pop()
            # mark the current space as visited
            maze[cur_row][cur_col] = -1
            for (dr,dc) in actions:
                new_row, new_col = cur_row, cur_col
                # let's move as long as either we hit a wall (space=1) or we go out of bound
                while 0 <= new_row + dr < nr and 0 <= new_col + dc < nc and maze[new_row + dr][new_col + dc] != 1:
                    new_row = new_row + dr
                    new_col = new_col + dc
                # if starting from any (cur_row,cur_col) we land at the destination we immediately return
                if [new_row, new_col] == destination:
                        return True
                # if not, we mark that destination as one that has already been visited and add it to the stack ...
                # ... to be used as a new starting point
                if maze[new_row][new_col] != -1:
                    maze[new_row][new_col] = -1
                    stack.append([new_row, new_col])
        # finally if no path is found, return False
        return False
        