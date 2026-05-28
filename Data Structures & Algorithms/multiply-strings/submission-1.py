class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {str(i):i for i in range(10)}
        print(dic)
        numOne, numTwo = 0, 0
        for i in range(len(num1)):
            numOne += dic[num1[i]] * 10 ** (len(num1)-i-1)

        for i in range(len(num2)):
            numTwo += dic[num2[i]] * 10 ** (len(num2)-i-1)

        print(numOne,numTwo)        

        product = numOne * numTwo
        print(product)

        return str(product)