# Question :- Angry Professor
"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
"""

# n = elements in arr
# k  = min. student to start the class


t = int(input().strip())



if t == 1:
    nk = input().rstrip().split()
    
    n = int(nk[0])
    k = int(nk[1])
    
    arr = list(map(int, input().rstrip().split()))
    
    a1 = []
    
    po = 0
    ne = 0

    
    for a in arr:
        if a <= 0:
            ne = ne+1
        if a > 0:
            po = po+1
            
    if ne >= k:
        ele = "NO"
        a1.append(ele)
    else:
        ele = "YES"
        a1.append(ele)
   
        
else:
    a1 = []
    for i in range(t):
        nk = input().rstrip().split()
    
        n = int(nk[0])
        k = int(nk[1])
        
        arr = list(map(int, input().rstrip().split()))
        
        
        po = 0
        ne = 0   
        
        for a in arr:
            if a <= 0:
                ne = ne+1
            if a > 0:
                po = po+1

                
        if ne >= k:
            ele = "NO"
            a1.append(ele)
        else:
            ele = "YES"
            a1.append(ele)

for i in range(t):
    print(str(a1[i]))
    
