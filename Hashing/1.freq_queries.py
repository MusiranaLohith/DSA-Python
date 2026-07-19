n = int(input("Enter the length of arr: "))
arr= []
for i in range(0,n):
    m = int(input())
    arr.append(m)
freq = [0] * 10

for i in range(len(arr)):
    freq[arr[i]] += 1
print(freq)

query = int(input("Enter the query: "))
print(freq[query])