import sys
import random
import math
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10**5)
outs = []

for __ in range(int(input())):
    n, = inp()
    tree={i:[] for i in range(1,n+1)}
    for _ in range(n-1):
        x,y = inp()
        tree[x].append(y)
        tree[y].append(x)

    def dfs(length,node,prev):
        ma = (length,node)
        for next in tree[node]:
            if next!=prev:
                (l,n2) = dfs(length+1,next,node)
                if l>ma[0]:
                    ma = (l,n2)
        return ma

    (l,start) = dfs(0,1,0)
    (dia_l,end) = dfs(0,start,0)

    dia = []
    def path(node,prev):
        
        if node == end:
            dia.append(node)
            return True
        else:
            for next in tree[node]:
                if next!=prev:
                    if path(next,node):
                        dia.append(node)
                        return True
    path(start,0)
    
    found=False
    
    for i in range(1,dia_l):
        if len(tree[dia[i]])>2:
            for n_di in tree[dia[i]]:
                if n_di!=dia[i-1] and n_di!=dia[i+1]:
                    a = dia[i-1]
                    b = dia[i]
                    c = n_di
                    found=True
                    break
        if found:
            break
    if found:
        outs.append(" ".join(map(str,[a,b,c])))
    else:
        outs.append(-1)
print("\n".join(map(str,outs)))