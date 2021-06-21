import sys


N = 4

"""
u, v, w = ([] for i in range(3))
for i in range(5):
    _u, _v, _w = [int(x) for x in input().split()]
    u.append(_u), v.append(_v), w.append(_w)
print(u, v, w)

u, v, w = [], [], []
for i in range(5):
    u[len(u):], v[len(v):], w[len(w):] = [[int(x)] for x in input().split()]
print(u, v, w)

u, v, w = [], [], []
for i in range(5):
    u[-1:-1], v[-1:-1], w[-1:-1] = [[int(x)] for x in input().split()]
    print(u, v, w)
u, v, w = [], [], []
u[len(u):-1], v[len(v):-1], w[len(w):-1] = [[int(x)] for line in sys.stdin.read().split('\n') for x in line.split() ]
print(u, v, w)

u, v, w = [], [], []
while s := input():
    u[len(u):0], v[len(v):0], w[len(w):0] = [[int(x)] for x in s.split()]
print(u, v, w)

u, v, w = ([0]*N for i in range(3))
for i in range(5):
    u[i], v[i], w[i] = [int(x) for x in input().split()]
    print(u, v, w)
"""

mat = [[int(x) for x in input().split()] for i in range(4)]
u, v, w =  zip(*mat)
print(mat)
print(u, v, w)

a, b, c, d ,e, f, g = ([] for _i in range(7))
for i in range(5):
    a[-1:-1] = [i]
    b[len(b)-1:len(b)-1] = [i]
    c[0:0] = [i]
    d[len(d):len(d)] = [i]
    e[len(e):0] = [i]
    f[len(f):-1] = [i]
    g[len(f):] = [i]
    print(a, b, c, d, e, f, g)

#  a[len(a):]形
