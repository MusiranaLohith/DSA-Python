# BRUTE FORCE
n = int(input())
result = []
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)
print(result)


# OPTIMIZED CODE
n = int(input())
result = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        result.append(i)
        if i != n//i:
            result.append(n//i)
    result.sort()
print(result)



