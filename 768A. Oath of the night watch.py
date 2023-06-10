steward = int(input())
position = list(map(int, input().split()))
position = sorted(position)
low = min(position)
high = max(position)
defects = []
if steward == 1:
    print("0")
    exit()
if low == high:
    print("0")
    exit(0)
x = 0
for u in range(steward):
    current = position[x]
    if current == low:
        defects.append(position[x])
    if current == high:
        defects.append(position[x])
    x = x + 1
list = len(position)
subtract = len(defects)
answer = list - subtract
print(answer)

