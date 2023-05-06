number = int(input())
name = input()
names = list(name)
a = 0
remove = 0
ex = 0
for x in range(number):
    if names[a] == "x":
        ex = ex + 1
        if ex >= 3:
            remove = remove + 1
    elif names[a] != "x":
        ex = 0
    a = a+1
    
print(remove)