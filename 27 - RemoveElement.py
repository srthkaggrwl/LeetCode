class Solution(object):
    def removeElement(self, nums, val):
        while True:
            try:
                i = nums.index(val)
                nums.pop(i)
            except Exception:
                break
        return nums        

solution = Solution()
print(solution.removeElement([3,2,2,3], 3))

 

'''
class Solution(object):
    def removeElement(self, nums, val):
        last_used_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_used_index] = nums[i]
                last_used_index += 1

        # The list nums[:last_used_index] contains the elements after removal
        return last_used_index

# Example usage:
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
new_length = solution.removeElement(nums, val)
print(nums[:new_length])  # Output: [2, 2]


'''
