lanterns, street = map(int, input().split())
position = list(map(int, input().split()))
position = sorted(position)
max_position = 0
current_position = 0
first_max = 0
last_max = 0

for i in range(1, len(position)):
    current_position = position[i] - position[i-1]
    if current_position > max_position:
        max_position = current_position

if lanterns == 1:
    
    if position[0] == 0:
        print('{0:.10f}'.format(abs(street - position[0])))
        exit()
        
    closestToStart = position[0] - 0
    closestToEnd = street - position[0] 

    if closestToStart > closestToEnd:
        print('{0:.10f}'.format(closestToStart))
        exit()
        
    else:
        print('{0:.10f}'.format(closestToEnd))
        exit()
        
if position[0] != 0:
    first_max = position[0]
    
if position[-1] != street:
    last_max = street - position[-1] 
    
max_position = max_position / 2
     
location = max(first_max, max_position, last_max)
print('{0:.10f}'.format(location))