class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a, max_b, max_c = 0, 0, 0

        target_a, target_b, target_c = target

        for triplet_a, triplet_b, triplet_c in triplets:
            if triplet_a > target_a or triplet_b > target_b or triplet_c > target_c:
                continue
            max_a = max(max_a, triplet_a)
            max_b = max(max_b, triplet_b)
            max_c = max(max_c, triplet_c)
        
        return [max_a, max_b, max_c] == target