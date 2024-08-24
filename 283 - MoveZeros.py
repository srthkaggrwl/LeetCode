class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        
        while True:
            try:
                i = nums.index(0)
                nums.pop(i)
            except Exception:
                break

        
        for i in range(len(nums), length):
            nums.append(0)

        return nums    





'''        last_non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0

        print(nums)            
   '''     
solution = Solution()
print(solution.moveZeroes([0,0])        )
        