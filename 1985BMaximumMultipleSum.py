testcase = int(input())
num = []
for x in range(testcase):
    integer = int(input())
    if integer > 3:
        integer = 2
    if integer == 0:
        integer = 0
    if integer == 1:
        integer = 1
    if integer == 3:
        integer = 3
    num.append(integer)
print(*num,sep='\n')
    