yellowc, bluec = input().split()
yellowc = int(yellowc)
bluec = int(bluec)
yellowb, greenb,  blueb = input().split()
yellowb, greenb, blueb = int(yellowb, greenb, blueb)
yellow = yellowb * 2 + greenb - yellowc
blue = blueb * 3 + greenb - bluec
if blue < 0:
    blue = 0
if yellow < 0:
    yellow = 0
need = blue + yellow

print(need)
