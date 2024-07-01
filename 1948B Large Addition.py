testcase = int(input())
for x in range(testcase):
    integer = int(input())
    digits = len(str(integer))
    onebyone = str(integer)
    if digits == 2:
        if integer >9 and integer < 19:
            print("YES")
        else:
            print("NO")
    if digits == 1:
        print("NO")
    if digits == 3:
        front = int(onebyone[0] + onebyone[1])
        back = int(onebyone[-1])
        if front >10 and front <20 and back <9:
            print("YES")
        else:
            print("NO")                    
    if digits > 3:
        front = int(onebyone[0] + onebyone[1])
        back = int(onebyone[-1])
        if front >10 and front <20 and back <9:
            isno = 0
            for x in range(len(onebyone)-3):
                if int(onebyone[x+2]) != 0:
                    continue
                else:
                    print("NO")
                    isno = 1
                    break
            if isno == 0:
                print("YES")
        else:
            print("NO")
    
      