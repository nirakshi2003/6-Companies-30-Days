from collections import defaultdict
class Solution:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.reset()

    def flip(self):
        i = randint(0, self.r)
        if self.nums[i] == -1:
            self.nums[i] = i
        if self.nums[self.r] == -1:
            self.nums[self.r] = self.r
        self.nums[i], self.nums[self.r] = self.nums[self.r], self.nums[i]
        self.r -= 1
        num = self.nums[self.r+1]
        return (num//self.n, num%self.n)

    def reset(self):
        self.r = self.m*self.n-1
        self.nums = defaultdict(lambda : -1)
