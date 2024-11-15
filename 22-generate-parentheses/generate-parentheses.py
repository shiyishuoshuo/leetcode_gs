class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def generateHelper(left:int, right:int, track:List[str]) -> None:
            if left > n or right > n:
                return 

            if left == n and right == n:
                res.append("".join(track))
                return
            
            if left < n:
                track.append('(')
                generateHelper(left + 1, right, track)
                track.pop()
            if left > right:
                track.append(')')
                generateHelper(left, right + 1, track)
                track.pop()


        res, path = [], []
        generateHelper(0, 0, path)
        return res
