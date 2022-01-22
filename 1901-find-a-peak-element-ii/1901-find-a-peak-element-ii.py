class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        h, w = len(mat), len(mat[0])
        
        top, bottom = 0, h - 1
        while top < bottom:
            mid = (top + bottom) // 2
            mid_row_max = max(mat[mid])
            upper_row_max = max(mat[mid - 1]) if mid - 1 >= 0 else -1
            lower_row_max = max(mat[mid + 1]) if mid + 1 < h else -1
            
            if mid_row_max > upper_row_max and mid_row_max > lower_row_max:
                return [mid, mat[mid].index(mid_row_max)]
            elif mid_row_max < upper_row_max:
                bottom = mid
            else:
                top = mid + 1
                
        return [top, mat[top].index(max(mat[top]))]