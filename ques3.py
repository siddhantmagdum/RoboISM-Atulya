def abc():
    a=int(input("Enter a number:"))
    b=input("enter an operator:")
    c=int(input("enter a number:"))
    if b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    elif b=='.':
        print(a*c)
    elif b=='/':
        print(a/c)
        abc()
while True:
    try:
        abc()
        break
    except:print ("Entered inputs are not valid\n")
