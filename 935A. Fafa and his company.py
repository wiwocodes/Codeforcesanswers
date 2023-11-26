employee = int(input())
ways = 0
number = 1
for x in range(employee):
    division = employee % number
    if division == 0:
        ways = ways + 1
        number = number + 1
    else:
        number = number + 1
ways = ways - 1
print(ways)