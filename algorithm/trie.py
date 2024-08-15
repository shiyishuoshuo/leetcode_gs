from typing import List

class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}

class TrieMap:

    def __init__(self):
        self.size = 0
        self.root = None

    # 在 Map 中添加 key
    def put(self, key: str, val):
        if not self.containsKey(key):
            self.size += 1

        def createTree(node: TrieNode, key: str, val: str, i: int):
            if not node:
                node = TrieNode()
            if i == len(key):
                node.val = val
                return node
            node.children[key[i]] = createTree(node.children.get(key[i]), key, val, i + 1)
            return node

        self.root = createTree(self.root, key, val, 0)

    # 删除键 key 以及对应的值
    def remove(self, key: str):
        if not self.containsKey(key):
            return

        def removeHelper(node: TrieNode, key: str, index: int):
            if not node:
                return None

            if index == len(key):
                node.val = None
            else:
                c = key[index]
                node.children[c] = removeHelper(node.children.get(c), key, index + 1)

            if node.val:
                return node

            for char, child in node.children.items():
                if child:
                    return node
            return None

        self.root = removeHelper(self.root, key, 0)
        self.size -= 1

    # 搜索 key 对应的值，不存在则返回 null
    # get("the") -> 4
    # get("tha") -> null
    def get(self, key: str):
        x = self.getNode(self.root, key)
        if not x or not x.val:
            return None
        return x.val

    # 从节点 node 开始搜索 key，如果存在返回对应节点，否则返回 null
    def getNode(self, node: TrieNode, key: str):
        p = node
        for c in key: 
            if not p:
                return None
            p = p.children.get(c)
        return p

    # 判断 key 是否存在在 Map 中
    # containsKey("tea") -> false
    # containsKey("team") -> true
    def containsKey(self, key: str) -> bool:
        return self.get(key) != None

    # 在 Map 的所有键中搜索 query 的最短前缀
    # shortestPrefixOf("themxyz") -> "the"
    def shortestPrefixOf(self, query: str) -> str:
        p = self.root
        for i in range(len(query)):
            if not p:
                return ""
            if p.val:
                return query[:i]
            p = p.children.get(query[i])
        if p and p.val:
            return query
        return ""

    # 在 Map 的所有键中搜索 query 的最长前缀
    # longestPrefixOf("themxyz") -> "them"
    def longestPrefixOf(self, query: str) -> str:
        p = self.root
        max_len = 0
        for i in range(len(query)):
            if not p:
                break
            if p.val:
                max_len = i
            p = p.children.get(query[i])
        if p and p.val:
            return query
        return query[:max_len]

    # 搜索所有前缀为 prefix 的键
    # keysWithPrefix("th") -> ["that", "the", "them"]
    def keysWithPrefix(self, prefix: str) -> List[str]:
        x = self.getNode(self.root, prefix)
        res, path = [], [prefix]
        if not x:
            return res
        def traverse(node: TrieNode, path: List[str], res: List[str]) -> None:
            if node:
                if node.val:
                    res.append("".join(path[:]))
                for c, child in node.children.items():
                    path.append(c)
                    traverse(child, path, res)
                    path.pop()
        traverse(x, path, res)
        return res

    # 判断是和否存在前缀为 prefix 的键
    # hasKeyWithPrefix("tha") -> true
    # hasKeyWithPrefix("apple") -> false
    def hasKeyWithPrefix(self, prefix: str) -> bool:
        return self.getNode(self.root, prefix) != None

    # 通配符 . 匹配任意字符，搜索所有匹配的键
    # keysWithPattern("t.a.") -> ["team", "that"]
    def keysWithPattern(self, pattern: str) -> List[str]:
        path, res = [], []

        def traverse(
            node: TrieNode, pattern: str, index: int, path: List[str], res: List[str]
        ):
            if not node:
                return
            if index == len(pattern):
                if node.val:
                    res.append("".join(path[:]))
                    return
            c = pattern[index]
            if c == ".":
                for char, char_child in node.children.items():
                    path.append(char)
                    traverse(char_child, pattern, index + 1, path, res)
                    path.pop()
            else:
                path.append(c)
                traverse(node.children[c], pattern, index + 1, path, res)
                path.pop()

        traverse(self.root, pattern, 0, path, res)
        return res

    # 通配符 . 匹配任意字符，判断是否存在匹配的键
    # hasKeyWithPattern(".ip") -> true
    # hasKeyWithPattern(".i") -> false
    def hasKeyWithPattern(self, pattern: str) -> bool:
        def hadKeyWithPatternHelper(node: TrieNode, index: int, pattern: str) -> bool:
            if not node:
                return False
            if index == len(pattern):
                return node.val
            c = pattern[index]
            if c != ".":
                return hadKeyWithPatternHelper(node.children.get(c), index + 1, pattern)
            for child, child_node in node.children.items():
                if hadKeyWithPatternHelper(child_node, index + 1, pattern):
                    return True
            return False

        return hadKeyWithPatternHelper(self.root, 0, pattern)

    # 返回 Map 中键值对的数量
    def size(self) -> int:
        return self.size


class TrieSet:
    def __init__(self):
        self.trie_map = TrieMap()

    def add(self, key: str):
        self.trie_map.put(key, 'V')

    def remove(self, key: str):
        self.trie_map.remove(key, 'V')

    def contains(self, key: str) -> bool:
        return self.trie_map.contains(key)

    def containsKey(self, key: str) -> bool:
        return self.trie_map.containsKey(key)

    def shortestPrefixOf(self, query: str) -> str:
        return self.trie_map.shortestPrefixOf(query)

    def longestPrefixOf(self, query: str) -> str:
        return self.trie_map.longestPrefixOf(query)

    def keysWithPrefix(self, prefix: str) -> List[str]:
        return self.trie_map.keysWithPrefix(prefix)

    def hasKeyWithPrefix(self, prefix: str) -> bool:
        return self.trie_map.hasKeyWithPrefix(prefix)

    def keysWithPattern(self, pattern: str) -> List[str]:
        return self.trie_map.keysWithPattern(pattern)

    def hasKeyWithPattern(self, pattern: str) -> bool:
        return self.trie_map.hasKeyWithPattern(pattern)

    def size(self) -> int:
        return self.trie_map.size()


class Trie:

    def __init__(self):
        self.trie_set = TrieSet()

    def insert(self, word: str) -> None:
        self.trie_set.add(word)

    def search(self, word: str) -> bool:
        return self.trie_set.containsKey(word)

    def startsWith(self, prefix: str) -> bool:
        return self.trie_set.hasKeyWithPrefix(prefix)


'''
Test case for TrieMap
'''

trie_map = TrieMap()

trie_map.put('them', 1)
trie_map.put('zip', 2)
trie_map.put('team', 3)
trie_map.put('the', 4)
trie_map.put('app', 5)
trie_map.put('that', 6)

assert trie_map.size == 6
assert trie_map.get('the') == 4
assert trie_map.get('them') == 1
assert trie_map.get('zip') == 2
assert trie_map.get('app') == 5
assert trie_map.get('something') == None

assert trie_map.containsKey("them") == True
assert trie_map.containsKey("app") == True
assert trie_map.containsKey("something") == False

assert trie_map.shortestPrefixOf('themxyz') == 'the'
assert trie_map.shortestPrefixOf('the') == 'the' # query was itself
assert trie_map.shortestPrefixOf('something') == '' # query was itself
assert trie_map.longestPrefixOf('themxyz') == "them"
assert trie_map.longestPrefixOf('them') == "them" # query was itself
assert trie_map.longestPrefixOf('something') == "" # query was itself

# print(f'{trie_map.keysWithPrefix("th")}')
assert set(trie_map.keysWithPrefix("th")) == set(["that", "the", "them"])
assert set(trie_map.keysWithPrefix("ak")) == set()

assert trie_map.hasKeyWithPrefix("app") == True
assert trie_map.hasKeyWithPrefix("th") == True
assert trie_map.hasKeyWithPrefix("apple") == False

# print(f'{trie_map.keysWithPattern("t.a.")}')
assert set(trie_map.keysWithPattern('t.a.')) == set(['team', 'that'])
assert set(trie_map.keysWithPattern('th..')) == set(['them', 'that'])
assert set(trie_map.keysWithPattern('them')) == set(['them'])

assert trie_map.hasKeyWithPattern(".ip")
assert trie_map.hasKeyWithPattern("app")
assert trie_map.hasKeyWithPattern("ap.")
assert not trie_map.hasKeyWithPattern(".i")

trie_map.remove('team')
assert trie_map.size == 5
assert trie_map.get('team') == None
assert trie_map.containsKey("app")
trie_map.remove('app')
assert trie_map.size == 4
assert trie_map.get('app') == None






