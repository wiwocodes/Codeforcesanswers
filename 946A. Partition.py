a = int(input())
D = []
D = input().split()
D = list(map(int,D))
pos = 0
neg = 0
x = 0
for y in D:
    print
    if D[x] > 0:
        pos = pos + int(D[x])
    else:
        neg = neg + int(D[x])
    x = x+1
max = pos - neg
print(max)