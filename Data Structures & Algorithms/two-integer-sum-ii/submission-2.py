class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # if n == 2:
        #     return [0,1]
        left = 0
        right = n-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target: 
                right -= 1
            else:
                break
        left_num = numbers[left]
        right_num = numbers[right]

        arr = [left+1, right+1]
        return arr
