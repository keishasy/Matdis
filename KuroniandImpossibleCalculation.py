def solve(n, m, a):
    if n > m:
        print(0)
        return

    a.sort()
    
    for i in range(1, n):
        if a[i] == a[i - 1]:
            print(0)
            return

    result = 1
    for i in range(n):
        for j in range(i + 1, n):
            result = (result * abs(a[i] - a[j])) % m
            if result == 0:
                print(0)
                return

    print(result)

n, m = map(int, input().split())
a = list(map(int, input().split()))
solve(n, m, a)
