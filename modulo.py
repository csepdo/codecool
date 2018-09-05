l = 0
top = 25
for i in range(1000, 100, -1):
    if i%7 == 0 or i%9 == 0:
        print(i)
        l += 1
        if l == top:
            break