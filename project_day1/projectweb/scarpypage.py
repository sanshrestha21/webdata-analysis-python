from datetime import datetime
import time
filename2 = time.strftime("%x")
print "namaste" + filename2
filename2 = time.strftime("%Y%m%d-%H%M%S")

print "hello" + filename2
print "----------------------"

filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
filename1 = time.strftime("%x")
#sys.stdout = open(filename1 + '.xml', 'w+')
f = open(filename1,'w+')
f.write(out)
f.close()