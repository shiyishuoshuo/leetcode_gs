class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        first, second = coordinates[0], coordinates[1]
        delta_y, delta_x = (second[1] - first[1]), (second[0] - first[0]) 

        for i in range(2, n):
            x, y = coordinates[i]
            if (x - second[0]) * delta_y != (y - second[1]) * delta_x:
                return False
            second = coordinates[i]
        return True
        