number = int(input())
x = []
x = input().split()
y = []
y = input().split()
z = 1
x.pop(0)
y.pop(0)

for l in range(number):
    if str(z) in x:
        z = z + 1
    elif str(z) in y:
        z = z + 1
    else:
        print("Oh, my keyboard!")
        exit()
print("I become the guy.")