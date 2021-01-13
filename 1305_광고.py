L = int(input())
ad = input()
Ad = []
for a in range(L):
    Ad.append(ad[a])

for l in range(1, L+1):
    Ex = Ad[:l]
    Test = []
    while len(Test) < L:
        for e in range(len(Ex)):
            Test.append(Ex[e])
    if Test == Ad:
        print(l)
        break
