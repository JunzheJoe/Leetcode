from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the input array to help with duplicate handling and two-pointer traversal
        nums.sort()
        
        # Result list to store unique triplets
        ans = []
        
        # Length of the array
        n = len(nums)

        # Step 2: Iterate through the sorted array
        for i in range(n - 2):  # We stop at n-2 because we need at least three numbers
            
            x = nums[i]  # Fixing the first number

            # Skip duplicate numbers to ensure unique triplets
            if i > 0 and x == nums[i - 1]:
                continue  # Move to the next unique number
            
            # Step 3: Apply Two Sum II with two pointers
            j = i + 1  # Left pointer
            k = n - 1  # Right pointer

            while j < k:
                s = x + nums[j] + nums[k]  # Compute the sum of three numbers
                
                if s > 0:
                    # If the sum is too large, decrease the right pointer to reduce the sum
                    k -= 1  
                elif s < 0:
                    # If the sum is too small, increase the left pointer to increase the sum
                    j += 1  
                else:
                    # If the sum is exactly 0, we found a valid triplet
                    ans.append([x, nums[j], nums[k]])
                    
                    # Move both pointers to avoid duplicates
                    j += 1
                    k -= 1
                    
                    # Skip duplicate values for j (left pointer)
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values for k (right pointer)
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1

        # Return the final list of unique triplets
        return ans
