class TrieNode:
    def __init__(self, value: int = -1):
        self.children = {}  # Initialize an empty dictionary for children
        self.value = value  # Store the value associated with the node

    def insert(self, path: str, value: int) -> bool:
        """
        Insert a path with its value into the trie.
        If path already exists or the parent doesn't exist, return False. Otherwise, insert and return True.
        """
        node = self
        # Split the path by '/' and iterate over the parts, excluding the first empty string and the last part
        parts = path.split("/")[1:-1]
        last = path.split("/")[-1]
        for part in parts:
            if part not in node.children:
                # If a part of the path doesn't exist, insertion is not possible
                return False
            node = node.children[part]
        if last in node.children:
            # If the last part of the path already exists, insertion is not possible
            return False
        # Otherwise, create the node for the new path and assign the value
        node.children[last] = TrieNode(value)
        return True

    def search(self, path: str) -> int:
        """
        Search for a path and return its associated value.
        If the path doesn't exist, return -1.
        """
        node = self
        # Split the path by '/' and iterate over the parts, excluding the first empty string
        for part in path.split("/")[1:]:
            if part not in node.children:
                # If a part of the path doesn't exist, the search is unsuccessful
                return -1
            node = node.children[part]
        return node.value  # Return the value of the final node


class FileSystem:
    def __init__(self):
        self.root = TrieNode()  # Initialize the file system with a root trie node

    def createPath(self, path: str, value: int) -> bool:
        """
        Public method to create a path with its value in the file system.
        Returns True if the path was successfully created, False otherwise.
        """
        return self.root.insert(path, value)

    def get(self, path: str) -> int:
        """
        Public method to get the value of a path in the file system.
        Returns the value if the path exists, -1 otherwise.
        """
        return self.root.search(path)

# Example usage:
fs = FileSystem()
assert fs.createPath("/a", 1)
assert fs.createPath("/a/b", 2)
assert fs.createPath("/a/b/c", 3)
assert fs.get("/a/b") == 2
assert fs.createPath("/a/b/c", 4) == False
assert fs.get("/a/b/c") == 3
assert fs.get("/d") == -1