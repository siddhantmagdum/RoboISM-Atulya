def abc():
    a=input("Enter a string    :")
    b=[]
    for i in a :
        b.append(i)
    b.sort()
    b=''.join(b)
    print(b)
abc()