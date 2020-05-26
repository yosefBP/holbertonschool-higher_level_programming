#!/usr/bin/python3
import sys


class NQueen:
    def __init__(self, n):
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.result = []

    def place(self, k, i):
        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.result.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.result

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
result = queen.nQueen(1)

for i in result:
    print(i)
