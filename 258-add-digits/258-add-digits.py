class Solution:
    def addDigits(self, num: int) -> int:
        def helper(num):
            if num<10:
                return num
            num=num%10+helper(num//10)
            if num>=10:
                return helper(num)
            return num
            
        return helper(num)