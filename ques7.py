def abc():
    try:
        a=list(map(int,input("Enter elements of the array     :").split()))
    except:
        print("Enter valid input")
        abc()
    b={}
    for i in a :
        if i in b :
            b[i]=b[i]+1
        else:
            b[i]=0
    print(max(b,key=b.get))
abc()