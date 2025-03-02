class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 相向双指针
        left = 0
        right = len(numbers) - 1 

        while left < right:
            sum = numbers[left] + numbers[right] 
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1] # 1-indexed array! 

        

        

        
        