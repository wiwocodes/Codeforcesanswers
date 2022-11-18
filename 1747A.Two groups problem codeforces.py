test = int(input())

for x in range(test):
    array = int(input())
    joe = 0;
    joe2 = 0;
    numbers = list(map(int, input().split()))
    for x in numbers:
   
        if x > 0:
        
          joe=joe + x;
        if x < 0:
          joe2=joe2 + x;
    addition = joe+joe2
    print(abs(addition))

#need forloop for testcase
#uno = numbers[:len(numbers)//2]
#dos = numbers[len(numbers)//2:]
#so tmr you need to find away to split the possitives and negatives into two diffrent lists then boom ur done (maybe?) or only have an even number of negatives in the right side
#uno = []
#dos = []
#numbers2 = list(map(str, input().split()))
#for i in range(0, len(numbers2)):
   # if(numbers2[i].startswith("-")):
  #      dos.append(str(numbers[i]))

#print(dos)
