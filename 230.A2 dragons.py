kirito, dragons = input().split()
a = []
b = []
c = []
dragons = int(dragons)
kirito = int(kirito)
for x in range(dragons):
    strength, bonus = input().split()
    strength = int(strength)
    bonus = int(bonus)
    a.append(strength)
    b.append(bonus)
c = zip(a, b)
c = list(c)

res = sorted(c, key = lambda x: x[0])

for l, n in res:
   d = 0
   e = 0
   d = l + d
   e = n + e
   int(d)
   int(e)
   if kirito > d:
        kirito = kirito + e
   else:
        print("NO")
        exit()
    
print("YES")
