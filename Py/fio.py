a = []
with open('in.txt') as f:
    N = int(f.readline())
    a[len(a):] = [[int(x) for x in f.readline().split()] for i in range(N)]
print(a)
