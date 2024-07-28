array=[]#creating a array

n=int(input("enter the number of elements "))

for i in range(0,n):
    ele=int(input("enter the elements "))#taking n number of inputs
    array.append(ele)

elep=int(input("the element to be found "))#input for element to be found
start=0
end=n-1
mid=(start+end)//2
if(array[mid]==elep):#element has been found 
    print("the element has been found ")

elif(array[mid]>elep):
    end=mid-1#like you wanted 25 so instead of 1 to 100 it will search 1 to 49(50-1)
elif(array[mid]<elep):
    start=mid+1#like you wanted 75 so instead of 1 to 100 it will search 51 to 100
else:
    print("the element is not present in the list")        