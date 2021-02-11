def BuyT(num, idx):
    while num > 0:
        Visited[idx] = 1
        num -= 1
        idx += 1

def FindMin(idx, Price):
    global N, Coupon, Min_P
    if idx == N:
        if Price < Min_P:
            Min_P = Price
        return
    if Price > Min_P:
        return
    for j in range(3):
        if T[j] == 1 and Coupon >= 3:
            Coupon -= 3
        else:
            Price += P[j]
        if T[j] == 3:
            Coupon += 1
        elif T[j] == 5:
            Coupon += 2
        BuyT(j, idx)


N, M = map(int, input().split(' '))
M_lst = list(map(int, input().split(' ')))
T = [1, 3, 5]
P = [10000, 25000, 37000]
Visited = [0]*N
Coupon = Price = 0
Min_P = 987654321

FindMin(0, 0)

print(Min_P)
