A=[1,22,34,23,23,12,12,323,12,13,99,123,1]

query=int(raw_input("Enter the value you want to search:"))
roun=0
real= True
for i in A:
    if i==query:
        print "Your query ", query, "is at ", roun, "on the database."
        
        real=False
    roun+=1


if real:
    print "None"