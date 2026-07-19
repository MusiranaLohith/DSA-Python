n = int(input("Enter the count of arr: "))
arr = []
for i in range(0,n):
    m = int(input())
    arr.append(m)
maximum = max(arr)
freq = [0] * (maximum+1)

for i in range(len(arr)):
    freq[arr[i]] +=1

query_count = int(input("Enter the number of queries: "))
j=0
for i in range(0,query_count):
    j = int(input("Enter the query: "))
    if j <= maximum:
        print("Frequency: ",freq[j])
    else:
        print("Invalid query")
