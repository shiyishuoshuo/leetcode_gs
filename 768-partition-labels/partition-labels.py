class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occurence_map = defaultdict(int)

        for i, char in enumerate(s):
            last_occurence_map[char] = i
        
        max_index, start_index = 0, 0

        partitions = []

        for index, c in enumerate(s):
            max_index = max(max_index, last_occurence_map[c])
            if index == max_index:
                partitions.append(index - start_index + 1)
                start_index = index + 1
        
        return partitions


        

        