
def check_if_float(x) -> bool:
    try:
        x = float(x)
    except:
        return False
    return True

def check_op(op) -> bool:
    opps = ["+", "/", "*", "-"]
    return op in opps

def calculator():
    while (True):
        x = input("What is your first value? ")
        if (check_if_float(x)):
            x = float(x)
            break
        else:
            print("Please input a number value. ")
    while (True):
        y = input("What is your second value? ")
        if (check_if_float(y)):
            y = float(y)
            break
        else:
            print("Please input a number value. ")
    while (True):
        op = input("What operation would you like to do on them? ")
        if (check_op(op)):
            break
        else:
            print("Please define operation as +, - ,/, or *. ")
    if op == "/":
        return x/y
    if op == "+":
        return x+y
    if op == "-":
        return x-y
    if op =="*":
        return x*y

print(calculator())

# notice the use of FLOAT instead of INT
    # float allows us to input numbers with decimals instead of just whole numbers