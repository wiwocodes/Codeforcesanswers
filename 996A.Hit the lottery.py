turns = 0
number = int(input())
joe = number
while number >= 100:
    joe = number // 100
    turns = turns + joe
    number = number - (joe*100)
while number >= 20:
    number = number - 20
    turns = turns + 1
while number >= 10:
    number = number - 10
    turns = turns + 1
while number >= 5:
    number = number - 5
    turns = turns + 1
while number != 0:
    number = number - 1
    turns = turns + 1
print(turns)