n = int(input("Enter the count of list: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
print("Before sorting: ",arr)
print()
for i in range(n-1):
    print(f"After Pass {i + 1}:")
    for j in range(0,n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
    print(arr)
print("Final Sorted arr: ",arr)