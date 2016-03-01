A=[]


try:
    while 1:
        A.append(int(raw_input("enter number if you have/enter non-integer to cancel. :")))
except:
    print A
    
for index in range(1, len(A)):
    key=A[index]

    print "key:", key,

    new= index-1
    if A[new]>key:
        while ( new>=0 ):
            print " new:", A[ new ]
            if A[new]>key:
                A[ new+1 ] = A[ new ]
                new = new-1
            else:
                A[ new+1 ] = key
                break
            A[new]=key
print A