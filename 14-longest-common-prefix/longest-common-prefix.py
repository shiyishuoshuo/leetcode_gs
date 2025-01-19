class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
    
    def addChild(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            self.count += 1


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.addChild(char)
            node = node.children[char]

        node.end = True

    def longestCommonPrefix(self, word):
        node = self.root
        res = []
        for char in word:
            if char in node.children and node.count == 1 and not node.end:
                res.append(char)
                node = node.children[char]
            else:
                break
        return "".join(res)


            


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        if len(strs) == 1:
            return strs[0]
        for str_ in strs:
            trie.insert(str_)
        return trie.longestCommonPrefix(strs[0])
        