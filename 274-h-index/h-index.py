class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def hasAtLeastHPapersWithHCitations(h, citations):
            return sum(1 for citation in citations if citation >= h) >= h

        low, high = 0, len(citations)

        while low <= high:
            mid = low + (high - low) // 2
            if hasAtLeastHPapersWithHCitations(mid, citations):
                low = mid + 1
            else:
                high = mid - 1
        
        return high