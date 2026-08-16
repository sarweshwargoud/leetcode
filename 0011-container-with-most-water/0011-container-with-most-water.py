class Solution:
    def maxArea(self, height):
        l=0
        r=len(height)-1
        max_area=0

        while l<r:

            width=r-l
            h=min(height[l],height[r])


            area=h*width
            max_area=max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area


















        # left = 0
        # right = len(height) - 1
        # max_area = 0

        # while left < right:

        #     h = min(height[left], height[right])
        #     width = right - left

        #     area = h * width
        #     max_area = max(max_area, area)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_area