testcase = input()
testcase = int(testcase)
for number in range(testcase):
    size, amount= input().split()
    size=int(size)
    amount=int(amount)
    for i in range(amount):
        x , y =(input().split())
        x=int(x)
        y=int(y)
    if amount >= size:
        print('NO')
    
    
    else:
        print('YES')
    