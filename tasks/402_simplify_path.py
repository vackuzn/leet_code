from enum import Enum


class Solution:
    def simplifyPath(self, p: str) -> str:
        dirs = [dir for dir in p.split("/") if dir]
        path_stack = []

        for d in dirs:
            if d == ".":
                pass
            elif d == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(d)
        
        return "/" + "/".join(path_stack)


inputs = {
    "/home/": "/home",
    "/home//foo/": "/home/foo",
    "/home/user/Documents/../Pictures": "/home/user/Pictures",
    "/../": "/",
    "/.../a/../b/c/../d/./": "/.../b/d",
}

for inp, expected in inputs.items():
    actual = Solution().simplifyPath(inp)
    assert actual == expected
