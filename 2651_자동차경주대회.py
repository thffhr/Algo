def FindMin(tf, k, n):
    global Min
    if n == C + 1:
        if Min > sum(Visited):
            Min = sum(Visited)
        return
    for c in range(n, C + 1):
        if tf or Distance[c] > k:
            Visited.append(Time[c - 1])
            k = K
        else:
            k -= Distance[c]
        FindMin(True, k, n + 1)
        Visited.pop()
        FindMin(False, k, n + 1)
K = int(input())
C = int(input())
Distance = list(map(int, input().split(' ')))
Time = list(map(int, input().split(' ')))
Visited = []
Min = 987654321

FindMin(True, 40, 1)
FindMin(False, 40, 1)