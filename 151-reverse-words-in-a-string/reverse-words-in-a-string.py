class Solution:
    def reverseWords(self, s: str) -> str:

        def trim_spaces(s:str) -> list:
            n = len(s)
            left, right = 0, n - 1
            while left <= right and s[left] == ' ':
                left += 1
            while right >= left and s[right] == ' ':
                right -= 1
            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output and output[-1] != ' ':
                    output.append(s[left])
                left += 1
            return output
        
        def reverse(l:list, left:int, right:int) -> None:
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        
        def reverseWords(l:list) -> None:
            n = len(l)
            start, end = 0, 0
            while start < n:
                while end < n and l[end] != ' ':
                    end += 1
                reverse(l, start, end - 1)
                start = end + 1
                end += 1

        res = trim_spaces(s)
        reverse(res, 0, len(res) - 1)
        reverseWords(res)

        return ''.join(res)
