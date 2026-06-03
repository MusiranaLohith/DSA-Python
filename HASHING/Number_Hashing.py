#BRUTE FORCE
n = [1,23,46,46,79,24,3,2,5,7,8,97,97,97]
m = [46,56,23,1,44,97,75,21]
for num in m:
    count = 0
    for x in n:
        if x == num:
            count +=1
    print(count)

# Optimized
n = [1,2,3,6,5,7,8,4,2,1,8,9,9,5]
m = [3,5,7,2,3,9,12,45]
hash_list = [0] * 11
for num in n:
    hash_list[num] += 1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])