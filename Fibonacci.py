num = int(input("Enter numbers required: "))
x, y = 0, 1
count = 1

if num > 1:
    print("Fibonacci series created-->")
    while count < num:
        print(x)
        n = x + y
        x = y
        b = n
        count += 1 
else:
    print("Series upto", num, ":")
    print(x)
