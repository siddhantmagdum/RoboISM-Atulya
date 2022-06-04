#i was not able to do this question so i took help of a friend
def fun():
    a=list(map(int,input("Enter the integer elements of the array with white spaces between them\n").split()))

    print (f"Before Swapping: a= {a[0]} b ={a[1]}")
    a[0] = a[0] ^ a[1]
    a[1] = a[0] ^ a[1]
    a[0] = a[0] ^ a[1]
    print (f"After Swapping: a= {a[0]} b ={a[1]}")
fun()