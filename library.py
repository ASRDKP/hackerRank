import os

stream = os.popen('pip list')

pip_list = stream.read()

Package=list(pip_list.split(" "))

c = 0
# for i in Package:
    # if "numpy" in i:
        # c = 1

# if c==1:
#     print("Module Installed")
# else :
#     print("Module is not installed")

li = []

for i in Package:
    li.append(i)
    
print("Installed Modules are : " )
print(li)    