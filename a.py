# Skip list

from random import randint, random

inf = float('inf')

class Node:
    def __init__(self, value, pnext = None, pdown = None):
        self.value = value
        self.pnext = pnext
        self.pdown = pdown

class SkipList:
    def __init__(self):
        right = Node(inf)
        left = Node(-inf, right)
        self.head = [left] 
        self.tail = [right]
        self.h = 0

    def predecessor(self, k):
        x = self.head[-1]
        while x.pdown != None:
            x = x.pdown 
            while x.pnext.value <= k:
                x = x.pnext
        return x.value

    def search(self, k):
        return self.predecessor(k) == k

    def insert(self, x):
        i = 0
        while random() < 0.5:
            i += 1
        for j in range(self.h + 1, i + 2):
            right = Node(inf, None, self.tail[j - 1])
            left = Node(-inf, right, self.head[j - 1])
            self.head.append(left)
            self.tail.append(right)
        self.h = max(i + 1, self.h)
        prec = None
        curr = self.head[i]
        while i >= 0:
            while curr.pnext.value < x:
                curr = curr.pnext
            n = Node(x, curr.pnext, None)
            if prec != None:
                prec.pdown = n
            curr.pnext = n
            prec = n 
            curr = curr.pdown
            i -= 1
   
    def delete(self, x):
        curr = self.head[-1]
        while curr.pdown != None:
            curr = curr.pdown
            while curr.pnext.value < x:
                curr = curr.pnext
            if curr.pnext.value == x:
                curr.pnext = curr.pnext.pnext

class EasySearch:
    def __init__(self):
        self.A = []

    def insert(self, c):
        self.A.append(c)

    def search(self, c):
        return c in self.A

    def delete(self, c):
        if not self.search(c):
            return
        del self.A[self.A.index(c)]

X = SkipList()
Y = EasySearch()
N = 10 ** 5
V = 1000
inserted = [False] * V
for i in range(N):
    value = randint(0, V - 1)
    request = randint(0, 2)
    if request == 0:
        ans1 = X.search(value)
        ans2 = Y.search(value)
        if ans1 != ans2:
            print("Error: ", inserted)
    elif request == 1:
        if inserted[value]:
            continue
        inserted[value] = True
        X.insert(value)
        Y.insert(value)
    else:
        inserted[value] = False
        X.delete(value)
        Y.delete(value)
