class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_len = len(words)
        mask = [0] * word_len

        for i in range(word_len):
            for ch in words[i]:
                mask[i] |= (1 << ord(ch) - ord('a'))
        
        res = 0


        for i in range(word_len):
            for j in range(i + 1, word_len):
              if mask[i] & mask[j] == 0:
                res = max(res, len(words[i]) * len(words[j])) 

        return res


        