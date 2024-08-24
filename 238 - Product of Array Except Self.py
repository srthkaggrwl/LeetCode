class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer    



solution = Solution()
print(solution.productExceptSelf([1,2,3,4])    )