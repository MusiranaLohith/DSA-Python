n = int(input("Enter the length of arr: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
print(arr)

temp = arr[0]
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] = temp
print(arr)
