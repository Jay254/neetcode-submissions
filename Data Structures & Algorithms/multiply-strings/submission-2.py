class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # dic = {str(i):i for i in range(10)}
        # print(dic)
        # numOne, numTwo = 0, 0
        # for i in range(len(num1)):
        #     numOne += dic[num1[i]] * 10 ** (len(num1)-i-1)

        # for i in range(len(num2)):
        #     numTwo += dic[num2[i]] * 10 ** (len(num2)-i-1)

        # print(numOne,numTwo)   
        #NEETCODE
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        res, beg = res[::-1], 0
        while res and res[beg] == 0:
            beg += 1

        res = map(str, (res[beg:]))

        return "".join(res)     

        product = numOne * numTwo
        print(product)

        return str(product)