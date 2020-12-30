N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
A = sorted(A)
B = sorted(B, reverse=True)

S = 0
for n in range(N):
    S += A[n]*B[n]

print(S)