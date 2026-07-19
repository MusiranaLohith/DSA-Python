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

max_freq = 0
answer = None
for key, value in freq.items():
    if value > max_freq:
        max_freq = value
        answer = key
print(f"Highest freq number is {answer}")
