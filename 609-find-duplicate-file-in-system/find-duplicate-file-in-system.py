class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        res = []
        file_map = defaultdict(set)

        for path in paths:
            file_paths = path.split(" ")
            file_path = file_paths[0]
            for f in file_paths[1:]:
                left, right = f.find("("), f.find(")")
                file_name, content = f[:left], f[(left + 1) : right]
                file_map[content].add(file_path + "/" + file_name)

        for val in file_map.values():
            if len(val) > 1:
                res.append(list(val))

        return res
