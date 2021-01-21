N, K = map(int, input().split(' '))
Arr = list(map(int, input().split(' ')))

num_sum = 0
for i in range(K):
    num_sum += Arr[i]
num_max = num_sum
for j in range(N-K):
    num_sum -= Arr[j]
    num_sum += Arr[K+j]
    if num_sum > num_max:
        num_max = num_sum

print(num_max)
