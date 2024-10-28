char=['A','B','C','D']
for i in range(len(char)):
    row=[]
    for j in range(i,-1,-1):
        row.append(char[j])
    print(row)
