height = int(input("height >>> "))
char = "*"
for x in range(0, height):
    print("{:>{height}}".format(char * ((x * 2) + 1), height=height + x))
