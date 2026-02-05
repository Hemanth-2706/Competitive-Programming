def solve():
    n = int(input())
    a = list(map(int, input().split()))
    r = n*(n+1)/2 - sum(a)
    print(int(r))

solve()