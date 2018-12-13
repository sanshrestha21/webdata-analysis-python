import time, os, datetime # fnmatch, shutil
from datetime import datetime

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H-%M-%S', t)
Filename = ("testfile-" + timestamp)
print Filename
print "-------------------"
#is_accessible = os.access("C:/programpython",os.F_OK)
#filename = "C:/programpython/myfile-%s.txt" %time.strftime('%Y-%m-%d')
filename=("timemachinefile-" + timestamp + ".html")
f = open(filename,"w+")
f.write("print line for testing ")
f.close()
print filename