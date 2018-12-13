import os,shutil
while True:
    line=raw_input("enter ur command:")
    tokens=line.split(" ")
    cmd=tokens[0].lower()
    if cmd=="md":
        
        if (len(tokens)>1):
            os.mkdir(tokens[1])
        else:
            print "syntax is error  "
    elif cmd=="rd":
        
        if (len(tokens)>1):
            os.rmdir(tokens[1])
        else:
            print "syntax is error  "
    elif cmd=="renjkjk":
        
        if (len(tokens)>2):
            shutil.move(tokens[1],tokens[2])
        else:
           print "syntax is error  " 
    elif(line=="exit"):
                exit()