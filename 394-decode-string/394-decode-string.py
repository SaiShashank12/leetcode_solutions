class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()

        for c in s:
            if c == "]":
                curString, number, i = "", 0, 0
                # 1. Get string
                while stack[-1] != "[":
                    curString = stack.pop() + curString
                stack.pop()
                # 2.Get number
                while stack and stack[-1].isnumeric():
                    number = int(stack.pop())*(10**i) + number
                    i += 1
                # 3. Append the result
                stack.append(curString*number)
            else:
                stack.append(c)

        return "".join(stack)
        