class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0 
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, area)
            
            if height[left] < height[right]: #短板效应(Bucket Effect)-> 哪边短移动哪边（详细原因见讲解视频）
                left += 1
            else:
                right -= 1
        return maxWater