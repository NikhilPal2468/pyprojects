#Python module for testing data structures- Arch 08/26/18

import sys
newstr = raw_input("Enter a string of length at least 5:")

while len(newstr)<5:
	newstr=raw_input("Error: Please enter again.")
print sys.getrefcount(newstr)     #why is refcount =2 here?
print "The string you entered:\'", newstr, "\'" #Gives space before and after
somestr= newstr
print sys.getrefcount(newstr)
#print "somestr=%7d newstr=%7d", newstr, somestr #Is also giving error

somestr[3]='Y'   #GIves error -"object does not support item assignment" 
                 #because strings are immutable 
print "somestr modified:", somestr
print sys.getrefcount(newstr)


