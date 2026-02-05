def solve():
    s = input()
    l = 1
    lst = []
    for i in range(len(s) - 1):
        if s[i+1] != s[i]:
            lst.append(l)
            l = 1
        else: l += 1
    lst.append(l)
    print(max(lst))

solve()