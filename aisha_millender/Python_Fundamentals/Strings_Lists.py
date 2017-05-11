str = "It's thanksgiving day. It's my birthday,too!"
print "find", str.find("day")
print "replace", str.replace("day","month", 1)

x = [2,54,-2,7,12,98]
print "min", min(x)
print "max", max(x)

orig_list = ["hello",2,54,-2,7,12,98,"world"]
new_list = [orig_list[0],orig_list[-1]]
print "new_list", new_list

list = [19,2,54,-2,7,12,98,32,10,-3,6]
list.sort()
print list
print list[0:5]
y = list[5:12]
print y
y[0] = list[0:5]
print y
