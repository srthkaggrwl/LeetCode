class Solution(object):
    def plusOne(self, digits):
        # Convert list of digits into an integer
        number = 0
        for digit in digits:
            number = number * 10 + digit
        
        # Increment the number by one
        number += 1
        
        # Convert the new number back to a list of digits
        new_digits = [int(ch) for ch in str(number)]
        return new_digits

# Example usage:
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
