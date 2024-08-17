class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        # make sure you understand dictionary compression here
        in_degrees = Counter({c : 0 for word in words for c in word})
        
        for first_word, second_word in zip(words, words[1:]):
            for first_char, second_char in zip(first_word, second_word):
                if first_char != second_char:
                    if second_char not in adj[first_char]:
                        adj[first_char].add(second_char)
                        in_degrees[second_char] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""

        queue = deque([c for c in in_degrees if in_degrees[c] == 0])
        output = []

        print(f'adj: {adj}')

        while queue:
            cur_char = queue.popleft()
            output.append(cur_char)
            for next_char in adj[cur_char]:
                in_degrees[next_char] -= 1
                if in_degrees[next_char] == 0:
                    queue.append(next_char)

        if len(output) < len(in_degrees):
            return ""

        return "".join(output)
        