class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        options = []
        res = []
        
        # turn string into graph "{a, b}c{d, e}f" -> [[a, b], [c], [d, e], [f]]
        while i < len(s):
            if s[i] == '{':
                tmpArr = []
                while s[i] != '}':
                    if s[i].isalpha():
                        tmpArr.append(s[i])
                    i += 1
                tmpArr.sort()
                options.append(tmpArr)
            elif s[i].isalpha():
                options.append([s[i]])
            i += 1
        
        # classic backtracking template
        def backtrack(index, tmpStr):
            if len(tmpStr) == len(options):
                res.append(tmpStr)
                return
            for s in options[index]:
                prev = tmpStr
                tmpStr += s
                backtrack(index + 1, tmpStr)
                tmpStr = prev
        
        backtrack(0, "")
        return res