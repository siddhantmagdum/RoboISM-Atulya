def abc():
    try:
        a=list(map(int,input("Enter elements of the array    :").split()))
    except:
        print("Enter a valid input")
        abc()
    a.sort()
    b=0
    c=0
    while((b+c)<(len(a)-1)):

        if a[b+c]==a[b+c+1]:
            print(str(a[b+c]))
            c=c+1
        else :
            pass
        b=b+1
abc()