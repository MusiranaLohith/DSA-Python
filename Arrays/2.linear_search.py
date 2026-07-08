n = int(input("Enter the length of arr: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
print(arr)

m = int(input("Enter the element to search: "))
target = m
gotIt = False
index = 0
for i in range(len(arr)):
    if arr[i] == target:
        gotIt = True
        index = i
        break

if gotIt:
    print(f"Element Found at index {index}")
else:
    print("Element not found")
