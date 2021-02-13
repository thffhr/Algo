def FindMin(idx, Visited, days, Price, Coupon):
    global aws
    if aws and Price > aws:
        return
    Visited[idx] = 1
    if idx+1 in M_lst:
        if days:
            FindMin(idx+1, Visited, days - 1, Price, Coupon)
        else:
            FindMin(idx + 1, Visited, days, Price, Coupon)
    else:
        if days:
            FindMin(idx+1, Visited, days - 1, Price, Coupon)
        else:
            for i in range(3):
                if idx + 1 < N:
                    if i == 0:
                        FindMin(idx + 1, Visited, days + T[i] - 1, Price + P[i], Coupon)
                        if Coupon >= 3:
                            FindMin(idx + 1, Visited, days + T[i] - 1, Price, Coupon - 3)
                    else:
                        if i == 1:
                            Coupon += 1
                        elif i == 2:
                            Coupon += 2
                        FindMin(idx+1, Visited, days+T[i]-1, Price+P[i], Coupon)
    if idx >= N - 1  and aws > Price:
        aws = Price
    if Visited[idx]:
        Visited[idx] = 0
    return


N, M = map(int, input().split(' '))
M_lst = list(map(int, input().split(' ')))
Visited = [0]*N
T = [1, 3, 5]
P = [10000, 25000, 37000]
aws = 987654321

FindMin(0, Visited, 0, 0, 0)

print(aws)
