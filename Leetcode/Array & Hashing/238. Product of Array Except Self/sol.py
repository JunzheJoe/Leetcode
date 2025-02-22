"""
nums = [1,2,3,4]
prefix_product = [1, 1*1, 1*1*2, 1*1*2*3]
postfix_product = [2*3*4, 3*4, 4, 1]
ouput = [24,12,8,6]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums) # 易错点：需要initialize成全1
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            output[i] = prefix  
            prefix *= nums[i] # 易错点：这一行代码不能在line 12代码之前

        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output


