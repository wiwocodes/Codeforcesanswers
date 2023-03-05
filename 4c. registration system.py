number = int(input())
data = {}
for x in range(number):
    names = input()
    if names not in data:
        data[names] = 0
        print("OK")
    else:
       data[names] = str(int(data[names])+1)
       print(names+data[names])
      
       data[names+data[names]] = 0
    