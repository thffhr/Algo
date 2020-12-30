switch_num, switch = int(input()), list(map(int, input().split()))
students = int(input())
s_print = ''

for i in range(students):
    g, n = map(int, input().split())
    if g == 1:
        for j in range(n, switch_num + 1, n):
            switch[j - 1] = (switch[j - 1] + 1) % 2
    else:
        for j in range(switch_num):
            if (n - j) > 0 and (n + j) <= switch_num:
                if (n - j) == (n + j):
                    switch[n - j - 1] = (switch[n - j - 1] + 1) % 2
                elif switch[n - j - 1] == switch[n + j - 1]:
                    switch[n - j - 1] = (switch[n - j - 1] + 1) % 2
                    switch[n + j - 1] = (switch[n + j - 1] + 1) % 2
                else:
                    break
            else:
                break

a = switch_num // 20
b = switch_num % 20
for i in range(a):
    print(*switch[(20 * i):(20 * (i + 1))])
print(*switch[(20*a):((20*a)+b+1)])
