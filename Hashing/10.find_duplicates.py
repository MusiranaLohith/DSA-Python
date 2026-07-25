n = int(input("Enter the count of arr: "))
arr = []
for _ in range(0,n):
    arr.append(int(input()))
freq = [0] * (n+1)

for i in range(len(arr)):
    freq[arr[i]] += 1
    if

print(freq)
