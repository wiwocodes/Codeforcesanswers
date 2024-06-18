paintings = 0
counter1 = 0
vertical = []
horizontal = []
n, m, k = list(map(int, input().split()))
array = [[0 for x in range(n)] for y in range(m)] 
arraynum = 0
#next time make the input multidimensional
def floodfill(row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return
    if region[row][col] != 0:
        return
    if museumMap[row][col] == '*':
        global paintings
        paintings += 1
        return
    array[row][col] = arraynum
    floodfill(row - 1, col)
    floodfill(row + 1, col)
    floodfill(row, col - 1)
    floodfill(row, col + 1)
    return
for i in range(m):
    counter2 = 0
    for i in range(n):
        array[counter1][counter2] = input()
        counter2 +=1
    counter1 +=1
for i in range(k):
    x, y = map(int, input().split())
  