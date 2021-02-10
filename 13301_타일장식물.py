N = int(input())
W = [1]
H = [1]
if N <= 1:
    print(4)
else:
    for n in range(1, N):
        if n%2:
            W.append(W[n-1]+H[n-1])
            H.append(H[n-1])
        else:
            W.append(W[n - 1])
            H.append(W[n - 1] + H[n - 1])

    print((W[-1] + H[-1]) * 2)
