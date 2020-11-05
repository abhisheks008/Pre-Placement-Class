test = int(input("Enter the number of test cases : "))
for i in range (0,test):
    n = int(input("Enter the value of N : "))
    total = 4*n
    m = n+1
    steps = total//m
    extra = total%m
    if (extra == 0):
        print("The number of moves needed : {}".format(steps))
    elif (extra>0):
        print ("The number of moves needed : {}".format(steps+1))
