number = int(input())
price = list(map(int, input().split()))
question = int(input())
adder = []
badder = []
listy = price.copy()
ascent = sorted(price)

for x in range(len(price)):
    current = price[x]
    if x == 0:
        previous = price[x-1]
    else:
        previous = adder[x-1]           
    
    total = current+previous  
    if x == 0:
        adder.append(current)
    else:
        adder.append(total)
for x in range(len(ascent)):
    current = ascent[x] 
    if x == 0:
        previous = price[x-1]
    else:
        previous = badder[x-1] 
    total = current+previous
    if x == 0:
        badder.append(current)
    else:
        badder.append(total)

for x in range(question):
    tipe, first, second = list(map(int, input().split()))
    
    if tipe == 1:
        if first == 1:
            
            print(adder[second-1])
        else:
            third = print(adder[second-1] - adder[first-2])
        
    if tipe == 2:
        if first == 1:
            print(badder[second-1])
        else:
            third = print(badder[second-1] - badder[first-2])

