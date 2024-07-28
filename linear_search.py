array=[]
n=int(input("enter the number of elements"))

for i in range(0,n):
    ele=int(input("enter the element"))
    array.append(ele)

print(array) #original arraay

tobefound=int(input("enter the elemet to be found"))

for i in range(0,n):
    if(array[i]==tobefound):
        print("element found at place ",i+1)

print("element not found")
