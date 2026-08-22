class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = heights[0]
        for i, height in enumerate(heights):
            idx = i
            while stack and height < stack[-1][1]:
                area = stack[-1][1]  * (i - stack[-1][0] )
                idx = stack [-1][0]
                max_area = max(area, max_area)
                stack.pop()

            stack.append([idx , height])

        
        length = len(heights)

        for bar in stack :
            area = bar[1] * (length - bar [0] )
            max_area = max(area, max_area)


        return max_area
