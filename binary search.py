array=[]

n=int(input("enter the number of elements "))

for i in range(0,n):
    ele=int(input("enter the elements "))
    array.append(ele)

elep=int(input("the element to be found "))
start=0
end=n-1
mid=(start+end)//2
if(array[mid]==elep):
    print("the element has been found ")

elif(array[mid]>elep):
    end=mid-1
elif(array[mid]<elep):
    start=mid+1
else:
    print("the element is not present in the list")        