# could def use memoization x dynamic programming

class Code:
    def __init__(self, l):
        self.l = ''.join(map(str, sorted(l, reverse=True)))

def answer(l):
    code = Code(l)
    print code.l

print answer([3,1,4,1])
