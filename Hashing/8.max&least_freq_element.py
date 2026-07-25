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

max_freq = float('-inf')
max_element = None

min_freq = float('inf')
min_element = None

for key,value in freq.items():
    if value > max_freq:
        max_freq = value
        max_element  = key
    elif value == max_freq:
        if key < max_element:
            max_element = key


    if value < min_freq:
        min_freq = value
        min_element = key
    elif value == min_freq:
        if key < min_element:
            min_element = key


print(f"The element with max frequency is {max_element} and the frequency is {max_freq}")
print(f"The element with min frequency is {min_element} and the frequency is {min_freq}")

