x=int(input ("enter the value of x:  "))

match x:
    case 0:
        print("x is zero")
    case 2:
        print("x is two")
    case _:
        print(x)

