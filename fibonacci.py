def fib():
    print("This is a way to show the fibonacci sequence.")
    n = eval(input("Input number to calculate the Fibonacci"))
    x,y = 1,0
    for i in range(n):
        print (x)
        #z = x + y
        #x = y
        #y = z
        x,y = y, x+y
fib()
