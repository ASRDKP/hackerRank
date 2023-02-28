q = int(input())

li = []

if q == 1:
    
    xyz = input().split()

    x = int(xyz[0])
    
    y = int(xyz[1])
    
    z = int(xyz[2])
    
    xz = abs(z-x)
    yz = abs(z-y)
    
    if xz < yz:
        ele = "Cat A"
        li.append(ele)
    elif xz > yz:
        ele = "Cat B"
        li.append(ele)
    else :
        ele = "Mouse C"
        li.append(ele)
else:
    for i in range(q):
        xyz = input().split()

        x = int(xyz[0])
        
        y = int(xyz[1])
        
        z = int(xyz[2])
        
        xz = abs(z-x)
        yz = abs(z-y)
        
        if xz < yz:
            ele = "Cat A"
            li.append(ele)
        elif xz > yz:
            ele = "Cat B"
            li.append(ele)
        else :
            ele = "Mouse C"
            li.append(ele)
            

for i in range(q):
    print(li[i])
            