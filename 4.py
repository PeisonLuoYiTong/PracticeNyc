#Ask user for 2 numbers, then print all values from the smaller to the larger value. For example if a=3 and b=6, print 3, 4, 5, 6. If a=8 and b=6, print 6, 7, 8.

a = int(input("input first number: "))
b = int(input("input second number: "))

#try, for loop, minimum and maximum of a,b. print.
#try:
#    for i in range(min(a,b),max(a,b)):
#        print(i)
#except:
#    print("error")

#for i in range(min(a,b),max(a,b)):
#    print(i, end=", ")

print("your values:")

#polishing
for i in range(min(a, b), max(a, b) + 1):
    if i != max(a, b):
        print(i, end=",")
    else:
        print(i, end=".")