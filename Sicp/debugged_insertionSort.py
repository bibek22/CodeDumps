A=[3,1,4,5,44,34,3444,222,3212,2]


# try:
#     while 1:
#         A.append(int(raw_input("enter number if you have/enter non-integer to cancel. :")))
# except:
#     print A
    
for index in range(1, len(A)):
    key=A[index]
    new= index-1
    print "round:", index
    if A[new]>key:
        while ( new>=0 ):
            if A[new]>key:
                A[ new+1 ] = A[ new ]
                print "put ", A[new], "in position ", new+1
            else:
                A[ new+1 ] = key
                print "put ", key, "in position ", new+1
                break
            A[new]=key
            new=new-1    
            print "put ", key, "in position", new
print A