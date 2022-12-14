tians = int(input())
for number in range(tians):
    monsters = int(input())
    health = [int(x) for x in input().split()]
    spell = [int(x) for x in input().split()]
    time = (sum(health)+sum(spell)-max(spell))
    print(time)