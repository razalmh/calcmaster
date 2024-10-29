print("welcomes to python basic project calculator")
x=int(input("for arithmetic calculation,provide the first number:"))
m=int(input("input second number for arithmetic calculation:"))
while True:
    h=input("provide arithmetic operator you need (*,+,-,/):")
    if h in ["*","+","-","/"]:
        if h=="*":
            print(x*m)
        elif h=="+":
            print(x+m)
        elif h=="-":
            print(x-m)
        else:
            if m!=0:
                print(x/m)
            else:
                print("Error: division by zero")
        break
    else:
        print("you provided the wrong arithmetic operator,please try again")
