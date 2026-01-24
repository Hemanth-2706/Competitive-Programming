"""
https://codeforces.com/gym/664897/problem/N
Date: 24-01-2026
"""

def solve():
    n,m=map(int,input().split())
    s = [int(x) for x in input()]
    a=list(map(int,input().split()))
    cum_sum = 0
    for x in a:
        cum_sum += x
        if cum_sum >= 0:
            continue
        elif -cum_sum < len(s):
            s = s[:len(s)+cum_sum]  # --->>> Avoid slicing lists inside loop. Insead keep track of how much to slice at the end.
            cum_sum = 0
        else:
            return "0"
    s = s + [0]*cum_sum
    return ''.join(str(x) for x in s)

t=int(input())
for _ in range(t):
    print(solve())