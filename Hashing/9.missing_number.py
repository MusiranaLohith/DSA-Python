n = int(input("Enter N: "))
arr = []
for _ in range(n-1):
    arr.append(int(input()))

freq = [0] * (n+1)

for i in range(len(arr)):
    freq[arr[i]] += 1
print(freq)

for i in range(1,n+1):
    if freq[i] == 0:
        print("Missing number is :",i)
