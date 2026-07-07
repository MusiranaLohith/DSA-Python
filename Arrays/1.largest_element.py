n = int(input("Enter the length of arr: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
print(arr)

largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("The largest element in the list or arr is: ",largest)
