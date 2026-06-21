class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w1,w2=0,len(heights)-1
        area = (min(heights[w1],heights[w2])*(w2-w1))
        while w1<w2:
            if heights[w1]<=heights[w2]:
                w1+=1
                new_area = (min(heights[w1],heights[w2])*(w2-w1))
            else :
                w2-=1
                new_area = (min(heights[w1],heights[w2])*(w2-w1))
            area = max(area,new_area)
        return area