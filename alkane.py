n=input("No. of C atoms: ")
m=input("Enter how many branches:")
l=[]
x=0
for i in range(m):
    a=input("Pos: ")
    l.append(a)

for i in range(n):
    if i!=(n-1):
        for j in l:
            if i+1==j:
                x=x+1
                if l.count(j)==2: 
                    print"C-C-C"
                    print"  |"
                else:
                    print"C-C"
                    print"  |"
                l.remove(j)
        if x==0:
            print"  C"
            print"  |"

        x=0
    else:
        print "  C"
