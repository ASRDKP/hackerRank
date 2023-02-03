nk = input().split()

n = int(nk[0])

k = int(nk[1])


height = input().split()
height.sort()

# print("N : ",n)
# print("K : ",k)
# print("Height : ", height)

x = int(height[len(height)-1])

if n == 100:
    if k >= x:
        print(0)
    else:
        print(abs(k-x) + 1)
else:
    if k >= x:
        print(0)
    else:
        print(abs(k-x))