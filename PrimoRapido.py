N = int(input())

for x in range(N):
    divisor = 0
    x = int(input())
    for y in range(x):
        if x%(y+1) == 0:
            divisor += 1

    if divisor == 2:
        print("Prime")
    else: 
        print("Not Prime")