class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stk = []
        output = [-1] * n

        for i in range(n - 1, -1, -1):
            while stk:
                j = stk[-1]
                if cars[i][1] > cars[j][1]:
                    time_to_collide = (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])

                    if output[j] == -1 or time_to_collide <= output[j]:
                        output[i] = time_to_collide
                        break
                stk.pop()
            stk.append(i)
        
        return output





        return output
        