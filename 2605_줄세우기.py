N = int(input())
Line = list(map(int, input().split(' ')))
Aws = []
for n in range(N):
    Aws.insert(n-Line[n], n+1)
aws = ''
for a in range(N):
    aws += str(Aws[a])+' '
print(aws[:-1])