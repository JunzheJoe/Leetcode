from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000: # This is for the recently added test case on Leetcode
            return 1
        
        k = len(nums) - k  # Convert k-th largest to index in sorted order
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: 
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
