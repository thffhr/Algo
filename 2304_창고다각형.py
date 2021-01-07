W = [0]*1000
max_L = max_H = result = 0
N = int(input())
for _ in range(N):
    L, H = map(int, input().split())
    W[L] = H
    # max_L = max(W)
    if max_L < L:
        max_L = L
    if max_H < H:
        max_H = H
        max_Hl = L

# 가장 높은 곳까지 창고 만들기
lm = 0
for i in range(max_Hl):
    if lm < W[i]:
        lm = W[i]
    elif lm >= W[i]:
        W[i] = lm
# 나머지 만들기
lm = 0
for i in range(max_L, max_Hl, -1):
    if lm < W[i]:
        lm = W[i]
    elif lm >= W[i]:
        W[i] = lm
# 더하기
for i in range(max_L+1):
    result += W[i]

print(result)



