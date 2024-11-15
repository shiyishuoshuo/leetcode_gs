class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def generateHelper(left:int, right:int, track:List[str], res: List[str]) -> None:
            if left > n or right > n:
                return 

            if left == n and right == n:
                res.append("".join(track))
                return
            
            if right > left:
                return
            
            track.append('(')
            generateHelper(left + 1, right, track, res)
            track.pop()

            track.append(')')
            generateHelper(left, right + 1, track, res)
            track.pop()


        res, path = [], []
        generateHelper(0, 0, path, res)
        return res
