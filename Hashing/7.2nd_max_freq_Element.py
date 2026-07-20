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
max_element = None

second_max_freq = 0
second_max_element = None

for key,value in freq.items():
    if value > max_freq:
        second_max_freq = max_freq
        second_max_element = max_element
        max_freq = value
        max_element = key
    elif value > second_max_freq and value < max_freq:
        second_max_freq = value
        second_max_element = key

if max_freq == second_max_freq:
    print("No second highest frequency")
else:
    print(second_max_freq)
    print(second_max_element)



