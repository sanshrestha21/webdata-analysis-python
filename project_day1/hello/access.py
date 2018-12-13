import sys
sys.path.append('../')
from project2.calculator import *

cal=calculator()
print cal.add(5,9)
print cal.sub(5,9)

print "----------------------"
si=simpleinterest()
si.p=200000
si.t=2
si.r=15

print "Interest %.2f"  %si.interest()
