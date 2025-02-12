from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the input list nums containing 0s, 1s, and 2s in-place.
        This implementation follows the Dutch National Flag Algorithm,
        ensuring a one-pass O(N) solution with constant O(1) space.
        """
        
        # Left pointer for tracking position of 0s
        l = 0
        # Right pointer for tracking position of 2s
        r = len(nums) - 1
        # Iterator pointer for traversing nums
        i = 0

        def swap(i, j):
            """Helper function to swap elements at indices i and j"""
            nums[i], nums[j] = nums[j], nums[i]

        # Process elements while i is within the right boundary
        while i <= r:
            if nums[i] == 0:
                # If current element is 0, swap it with the leftmost boundary
                swap(i, l)
                l += 1  # Move left pointer forward
                i += 1  # Move iterator forward
            elif nums[i] == 2:
                # If current element is 2, swap it with the rightmost boundary
                swap(i, r)
                r -= 1  # Move right pointer backward
                # Do not increment `i` because we need to check the swapped element
            else:
                # If nums[i] is 1, it's already in the correct position, move forward
                i += 1
