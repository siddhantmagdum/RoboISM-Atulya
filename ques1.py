def abc():
    while True:

        try:
            x=list(map(int,input("Enter all elements of list    :\n").split()))
            break
        except:
            print("enter a valid input\n")

    def abc():
        a=(input("\nEnter 'asc','desc' or 'none'"))
        if a=="none":
            pass
        elif a=="asc":
            x.sort()
        elif a == "desc":
            x.sort(reverse=True)
        else :
            print("cannot give the output...")
            rec()
    abc()
    print("The required form of the list is    :"+str(x))
fun()