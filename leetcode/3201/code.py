import functools
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        alt = 1

        if nums[0] % 2 == 1:
            odd += 1
        else:
            even += 1

        previous = nums[0]
        for index in range(1, len(nums)):
            if nums[index] % 2 == 1:
                odd += 1
            else:
                even += 1
            if previous % 2 != nums[index] % 2:
                alt += 1

            previous = nums[index]

        return max(odd, even, alt)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4]
    print(f"Should be 4: {solution.maximumLength(nums)}")

    # Example 2
    nums = [1,2,1,1,2,1,2]
    print(f"Should be 6: {solution.maximumLength(nums)}")

    # Example 3
    nums = [1, 3]
    print(f"Should be 2: {solution.maximumLength(nums)}")
