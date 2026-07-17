n = int(input("Enter the count of arr: "))
arr = []
for i in range(0,n):
    m = int(input())
    arr.append(m)

maximum = max(arr)
freq = [0] * (maximum+1)

for i in range(len(arr)):
    freq[arr[i]] += 1
print(freq)
max_freq = freq[0]
max_element = 0
for i in range(len(freq)):
    if freq[i] > max_freq:
        max_freq = freq[i]
        max_element = i
print("Highest freq element:", max_element)
print("Frequency: ",max_freq)


