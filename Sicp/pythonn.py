n=1
while (100*n*n >= 2**n):
    n+=1
    print n
    if (100*n*n <= 2**n):
        print n
        break

print n