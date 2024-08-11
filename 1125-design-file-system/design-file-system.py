class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1

class TrieFileSystem:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path, value):
        cur = self.root
        paths = path.split("/")[1:]
        for i, path in enumerate(paths):
            if path not in cur.children:
                if i == len(paths) - 1:
                    cur.children[path] = TrieNode()
                else:
                    return False 
            cur = cur.children[path]
        if cur.value != -1:
            return False
        cur.value = value
        return True

    def search(self, path):
        cur = self.root
        paths = path.split("/")[1:]
        for path in paths:
            if path not in cur.children:
                return -1
            cur = cur.children[path]
        return cur.value

class FileSystem:

    def __init__(self):
        self.trie_file_system = TrieFileSystem()
        

    def createPath(self, path: str, value: int) -> bool:
        return self.trie_file_system.insert(path, value)
        

    def get(self, path: str) -> int:
        return self.trie_file_system.search(path)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)