necklace = input()

strings = necklace.count('-')


pearls = necklace.count('o')

if pearls ==0:
    print("yes")
elif strings ==0:
    print("yes")
elif (strings%pearls) ==0:
    print("Yes")

else:
    print("No")
    