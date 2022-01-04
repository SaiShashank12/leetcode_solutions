class Solution:
    def bitwiseComplement(self, n: int) -> int:
        dir1=str(bin(n)[2:])
        result=[]
        for i in dir1:
            x='0' if i=='1' else '1'
            result.append(x)
        def binaryToDecimal(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return decimal 
        str1="".join(result)
        print(str1)
        return binaryToDecimal(int(str1))
        #print(result)
        