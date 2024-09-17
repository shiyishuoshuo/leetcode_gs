class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        num_words = len(words)

        for row, word in enumerate(words):
            for col, c in enumerate(word):
                if col >= num_words or row >= len(words[col]) or c != words[col][row]:
                    return False
        
        return True





            
        