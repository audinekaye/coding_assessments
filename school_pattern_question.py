import sys

o = "o"
x = "x"
numLines = int(input("Enter the number of lines you would like in your pattern: \n"))

if numLines > 9:
    sys.exit("Too many lines! Enter less")
else:
    for i in range(1,numLines+1):
        p = (numLines - i) + 1
        print((x * p) + (o * i))
