def sam(x,y):
    lambda x,y : x*y
    x = 10
    y = 12
    if (x > y):
        print("the greater number is: " + str(x))
    else:
        print("the greater number is: " + str(y))

sam(10,12)

sam = lambda x,y : x*y
print(sam(8,9))