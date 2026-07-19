n = int(input("Enter the count of arr: "))
arr = []
for i in range(0,n):
    m = int(input())
    arr.append(m)

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key,value in freq.items():
    print(key,":",value)