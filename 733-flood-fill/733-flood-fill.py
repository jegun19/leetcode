class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        def changeColor(sr, sc, color, newColor):
            if 0 <= sr < m and 0 <= sc < n:
                # Change color
                if image[sr][sc] == color:
                    image[sr][sc] = newColor
                    changeColor(sr-1, sc, color, newColor)
                    changeColor(sr+1, sc, color, newColor)
                    changeColor(sr, sc-1, color, newColor)
                    changeColor(sr, sc+1, color, newColor)

        
        startColor = image[sr][sc]
        if startColor == newColor:
            return image
        else:
            changeColor(sr, sc, startColor, newColor)

        
        return image