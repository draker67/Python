#Author: Sarath
#Program: To evaluate whether a given matrix is reflexive


# read matrix

matrix=[[1,1,1],
        [1,1,1],
        [1,1,1]]

#Funtion to check if reflexive

def reflexive(matrix):
    ref=True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(i==j):
                if(matrix[i][j]!=1):
                    ref=False
    return ref

#Function to check if matrix is symmetric

def symmetric(matrix):
    sym=True
    for i in range(len(matrix)):
        if(len(matrix)!=len(matrix[i])):
            sym=False
    return sym






if(symmetric(matrix)):
    if(reflexive(matrix)):
        print("true")
    else:
        print("false")
else:
    print("Matrix is not symmetric")
