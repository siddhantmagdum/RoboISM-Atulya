def abc():
    while True:
            x=input("Enter credit card number    :")
            if (len(x)==16):
               break
    b="************"
    for a in range(0,4):
        b=b+str(x[a+12])
    print(b)
abc()
