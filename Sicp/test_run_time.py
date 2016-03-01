def seq(num):
    count=0
    while(num!=1):
        if(num%2==0):
            num/=2
        else:
            num=num*3+1
        count+=1
    return count
flag=0
result=0
for i in range(1,1000000):
    if(seq(i)>flag):
        flag=seq(i)
        result=i
print result