w, h = map(int, input().split(' '))
p, q = map(int, input().split(' '))
t = int(input())

# 앞으로 갈 거리 p + t / q + t
# w / h 로 나눈 값이 홀수일 경우 0부터 w / h 까지 증가
# 아닐 경우 w / h 부터 0으로 감소
if ((p + t) // w) % 2:
    x = w - ((p + t) % w)
else:
    x = (p + t) % w

if ((q + t) // h) % 2:
    y = h - ((q + t) % w)
else:
    y = (q + t) % h

print(x, y)
# p_plus = q_plus = 1
# for t in range(T):
#     if p + p_plus > w or p + p_plus < 0:
#         p_plus *= -1
#     if q + q_plus > h or q + q_plus < 0:
#         q_plus *= -1
#     p += p_plus
#     q += q_plus
#
# print(p, q)