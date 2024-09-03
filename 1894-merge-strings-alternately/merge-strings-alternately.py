class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointer 
        p, q = 0, 0
        res = []
        is_word1 = True

        while p < len(word1) and q < len(word2):
            if is_word1:
                res.append(word1[p])
                p += 1
            else:
                res.append(word2[q])
                q += 1
            is_word1 = not is_word1
        
        if p == len(word1):
            res.append(word2[q:])

        if q == len(word2):
            res.append(word1[p:])

        return ''.join(res)
            



        
        