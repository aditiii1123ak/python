def matrix (m, n):
    o=[]
    for i in range (m):
        row=[]
        for j in range (n):
            inp=int(input("enter 0[(i)][(j)]"))
            row.append(inp)
        o.append(row)
    return o
def sum(A,B):
    output=[]
    for i in range (len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] *B[i] [j])
        output.append(row)
    return output
m=int(input("Enter value of m\n"))
n=int(input("Enter value of m\n"))
print("Enter matrix A")
A=matrix (m,n)
print(A)
print("Enter matrix B")
B=matrix(m, n)
print(B)
s=sum (A, B)
print (s)
                
