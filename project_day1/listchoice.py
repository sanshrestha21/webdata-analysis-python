import sys
names=[]
i=1
while(True):
    print ("1. Enter ur name:")
    print ("2. Show all name list")
    print ("3. Exit")
    choice=input("Enter ur choice:")
    if choice==1:
        name=raw_input("Enter ur name:")
        names.append(name)

    elif choice==2:
        for n in names:
            print n
    elif choice==3:
        sys.exit(0)
while(i==0):
        print ("Input correct choice value")
        sys.exit(0)