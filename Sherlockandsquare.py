import math

q = int(input().strip())

li = []

for _ in range(q):
    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])
    
    count = 0
    
    # for i in range(1, b+1):
    #     if (i*i) >= a and (i*i) <= b:
    #         count = count + 1
    
    count = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    
    li.append(count)
    
for i in range(q):
    print(li[i])
