number = int(input())
teams = list(map(int, input().split()))
y = 0
for x in range(len(teams)):
    current = teams[x]
    elif x < number-1:
        nexus = teams[x+1]
    if current == 0 :
        y=y+1
        print(str(y)+"0")
        continue
     
    elif (current % 2) == 0: 
        y=y+1
        print(str(y)+"2")
        continue
    
        if (current % 2) == 1 and (nexus % 2) == 1:
            teams[x+1] = teams[x+1]-1
            y=y+1
            print(str(y)+"1")
            continue
       
        
    
    
if y == number:
    print("YES")
else:
    print("NO")