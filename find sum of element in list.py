lit=[]
n=int(input("Enter the number"))
for i in range (0,n):
    num=int(input("Enter any number"))
    lit.append(num)
print (lit)
total=0
for num in range (0,len(lit)):
    total=total+lit[num]
print ("Sum=",total)
