def FindMax(arr, n):
    max_num = 0
    for i in range(1 << n):
        Subset = []
        for j in range(n):
            if i & (1 << j):
                Subset.append(arr[j])
        if len(Subset) == 3:
            num_sum = sum(Subset) % 10
            if num_sum > max_num:
                max_num = num_sum
    return max_num

N = int(input())
Card_Num = []
for _ in range(N):
    Card_Num.append(list(map(int, input().split(' '))))

num_lst = []
for n in range(N):
    num_lst.append(FindMax(Card_Num[n], 5))

aws_num = max(num_lst)
aws = 0
for n in range(N):
    if num_lst[n] == aws_num:
        aws = n+1

print(aws)
