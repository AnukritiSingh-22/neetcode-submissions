class Solution:
    def maxArea(self, heights: List[int]) -> int:
        w1,w2=0,len(heights)-1
        area = (min(heights[w1],heights[w2])*(w2-w1))
        while w1<w2:
            print(area)
            if heights[w1]<=heights[w2]:
                w1+=1
                new_area = (min(heights[w1],heights[w2])*(w2-w1))
                print("area after small shift :", new_area)
                print("max area = ", area)
            else :
                w2-=1
                new_area = (min(heights[w1],heights[w2])*(w2-w1))
                print("area after big shift :", new_area)
            area = max(area,new_area)
            print("max area = ", area)
        return area