flights, gap = input().split()
flights=int(flights)
gap=int(gap)
currenthour = 0 
currentminute = 0
nexthour = 0
nextminute = 0
#List of Hour, Minutes Landing Schedules
hour = []
minutes = []
space = gap * 2

for number in range(flights):
    x , y =(input().split())
    x=int(x)
    y=int(y)
    hour.append(x)
    minutes.append(y)

if hour[0] > 0 and hour[0] < 2 and space < 60:
    print(str(0) + " " + str(0))
    exit()

if minutes[0] >= (gap+1):
    print(str(0) + " " + str(0))
    exit()
if hour[0] > 1:
    print(str(0) + " " + str(0))
    exit()

    
for x in range(len(hour)):
    currenthour = hour[x]
    currentminute = minutes[x]
    c = currenthour
    
    
    if x != len(hour)-1:
        nexthour = hour[x+1]
        nextminute = minutes[x+1]

    d = currentminute + space + 2
    
    if d > 119:
        c = currenthour + 2
        d = d - 120
    
    elif d > 60 and d < 120:
        c = currenthour + 1
        d = d - 60
        
    if c < nexthour:
        h = currenthour
        g = currentminute + gap + 1
        
        if g > 59 and g < 120:
           h = currenthour + 1
           g = g - 60
        if g > 119:
            h = currenthour + 2
            g = g - 120
           
        print(str(h) + " " + str(g))
        exit()
        
    elif d<=nextminute and c==nexthour:
        h = currenthour
        g = currentminute + gap + 1
       
        if g > 59 and g < 120:
           h = currenthour + 1
           g = g - 60
        if g > 119:
            h = currenthour + 2
            g = g - 120
           
           
        print(str(h) + " " + str(g))
        exit()

afterHour = hour[-1]
afterMins = minutes[-1] + gap + 1

if afterMins > 59 and afterMins < 120:
    afterHour = hour[-1] + 1
    afterMins = afterMins - 60
if afterMins > 119:
    afterHour = hour[-1] + 2
    afterMins = afterMins - 120
    
print(str(afterHour) + " " + str(afterMins))