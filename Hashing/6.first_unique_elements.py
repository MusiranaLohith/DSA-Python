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

answer = None
for num in arr:
    if freq[num] == 1:
        answer = num
        print(answer)
        break

if answer is None:
    print("No first unique element")