import math
import datetime

class XORShift:

    def __init__(self, seed = datetime.datetime.now().microsecond):
        self.state = seed
    
    def xorshift(self):
        self.state ^= (self.state << 13) & 0xFFFFFFFF
        self.state ^= (self.state >> 17) & 0xFFFFFFFF
        self.state ^= (self.state << 5) & 0xFFFFFFFF
        return self.state
    
    def rand(self):
        return self.xorshift() / 0x100000000
    
    def randint(self, mn: int, mx: int):
        return math.floor(self.rand() * mx) + mn
    
    def shuffle(self, arr):
        n = len(arr)
        for i in range(n):
            pos = self.randint(0, n-1)
            arr[i], arr[pos] = arr[pos], arr[i]
    
    def choice(self, arr):
        return arr[self.randint(0, len(arr))]
