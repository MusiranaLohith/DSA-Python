n = int(input("Enter the length of arr: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
print(arr)

reverse = n-1
for i in range(n // 2):
    temp = arr[i]
    arr[i] = arr[reverse]
    arr[reverse] = temp
    reverse -= 1
print(arr)