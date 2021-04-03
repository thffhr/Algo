def FindAllNums(start, depth):
    if depth <= 0:
        for n in Num_lst:
            print(n, end=' ')
        print('')
        return
    for i in range(start, len(S)):
        Num_lst.append(S[i])
        FindAllNums(i+1, depth-1)
        Num_lst.pop()

Num_lst = []
tc = True
while tc:
    answer = []
    S = list(map(int, input().split(' ')))
    if len(S) == 1:
        tc = False
        break
    K = S.pop(0)
    S.sort()
    FindAllNums(0, 6)
    print('')