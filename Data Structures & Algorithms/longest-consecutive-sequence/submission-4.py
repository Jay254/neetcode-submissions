class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        #[2,3,4,4,5,10,20] => [2,3,4,5] - 4 numbers 
        # [0,1,1,2,3,4,5,6][0, 1, 2,3,4, 5, 6] - 7 numbers

        #sort the array
        #nums.sort()
        nums_sorted = sorted(set(nums))
        print(nums_sorted[0])
        # [2,3,4,5,10,20]
        # [0,1,2,3,4,5,6]
        arr = []
        count = 1
        leng = len(nums_sorted)
        for i in range(1,leng):
            if nums_sorted[i] - nums_sorted[i-1] == 1:
                count += 1
            else:
                arr.append(count)
                count = 1
        arr.append(count)
#[4,2]  
#[6]

        return max(arr)
            