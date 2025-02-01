def editString(s: str) -> str:
    ptr = len(s) - 1
    store = ""
    counter = 0
    while ptr >= 0:
        if s[ptr] == '#':
            counter += 1
        elif counter != 0:
            counter -= 1
        else:
            store = store + s[ptr]
        ptr -= 1
    return store

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = editString(s)
        t = editString(t)
        print(s, t)
        return s == t