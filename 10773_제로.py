K = int(input())
stack = []
num_sum = 0

while K > 0:
    K -= 1
    num = int(input())
    if num:
        stack.append(num)
        num_sum += num
    else:
        num_sum -= stack[-1]
        stack.pop()

print(num_sum)
