def getH(root):
    for n in range(N):
        if Info[n][0] == root:
            Tree_H.append([Info[n][0]])
        getH(Info[n][1])
        break
    return

N = int(input())
Info = [list(map(int, input().split(' '))) for _ in range(N)]
Tree_w = [Info[0][0]]
Tree_H = []

for i in range(N):
    if Info[i][1] > 0:
        Tree_w.insert(Tree_w.index(Info[i][0]), Info[i][1]) # 왼쪽자식
    if Info[i][2] > 0:
        Tree_w.insert(Tree_w.index(Info[i][0]) + 1, Info[i][2]) # 오른쪽자식

getH(1)
print(Tree_H)
#
# print(len(Tree_w))

