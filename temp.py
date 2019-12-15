import random
mat=[]




for r in range (3):
    roll=[]
    for c in range(3):
        roll.append("~")
    mat.append(roll)
#print (mat)


for i in range(3):
    for h in range (3):
        print ("\t",mat[i][r],"\t",end="")
    print()
        

