class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.linkedCount = 0

    def addChild(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
            self.linkedCount += 1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.addChild(c)
            cur = cur.children[c]
        cur.endOfWord = True

    def searchLongestCommonPrefix(self, word) -> str:
        node = self.root
        res = []
        for char in word:
            if char in node.children and node.linkedCount == 1 and not node.endOfWord:
                res.append(char)
                node = node.children[char]  
            else:
                break
        return ''.join(res)

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trieTree = Trie()
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs)):
            trieTree.insertWord(strs[i])
        return trieTree.searchLongestCommonPrefix(strs[0])
        
        