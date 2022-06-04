def abc():
    a=input("Enter a string     :")
    b=0
    for i in a:
        try:
            b=b + int(i)
        except:
            pass
    print(b)
abc()