H, W = map(int, input().split(' '))
Map = list(map(int, input().split(' ')))
count = 0

for h in range(H):
    for w in range(1, W-1):
        if Map[w-1] > Map[w] and Map[w+1] > Map[w]:
            count += 1
            Map[w] += 1
        elif Map[w-1] > Map[w] and Map[w+1] == Map[w]:
            k = w+1
            while k < W:
                if Map[k] > Map[w]:
                    count += 1
                    Map[w] += 1
                    break
                else:
                    k += 1

print(count)