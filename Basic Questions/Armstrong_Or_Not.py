a = int(input())
num = a
result = 0
digits = len(str(a))
while num>0:
    n = num%10
    result += n ** digits
    num = num//10
if a == 0:
    print("Armstrong")
elif result == a:
    print("Armstrong")
else:
    print("Not Armstrong")
