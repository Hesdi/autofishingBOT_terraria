N, M = map(int, input().split())

sol =

m = M//2

Nums = list(map(lambda x: input(), range(N)))

for i in Nums:
    n = i.split()
    map_obj = map(int, n)
    l = list(map_obj)
    l.sort()
    mid = l[m]