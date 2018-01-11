#move disks from A to B using C as AUX
global num
#function that gives the solution to the hanoi problem
def hanoi (n,A,B,C):  
	if n==0:
		print "Move disk %s from %s to %s"  %(num-n-1,A,B)  
	else:
		hanoi(n-1,A,C,B)     #recursion
		print "Move disk %s from %s to %s" %(num-n-1,A,B)
		hanoi (n-1,C,B,A)      #recursion
      

#input the number of disks
num = input ("Enter the number of disks :")
a= "A"
b= "B"
c= "C"
hanoi (num,a,a,c)    #calling function

