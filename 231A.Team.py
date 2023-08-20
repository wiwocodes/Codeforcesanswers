problems = int(input())
solve = 0
for x in range(problems):
    one, two, three = map(int, input().split())
    four = one + two + three
    if four > 1:
        solve = solve + 1
    
print(solve)