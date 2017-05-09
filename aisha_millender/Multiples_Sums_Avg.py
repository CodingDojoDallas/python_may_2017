#multiples part I
for count in range(0,1001):
    if count % 2 != 0:
        print "counting - ", count

#multiples part II
for multiple in range(0,1000001):
    if multiple % 5 == 0:
        print "multiple - ", multiple

#sum list
a = [1,2,5,10,255,3]
print sum(list(a))

#avg list
b = [1,2,5,10,255,3]
import numpy as np
print np.mean(b)

#or
b = [1,2,5,10,255,3]
print sum(b) / float(len(b))
