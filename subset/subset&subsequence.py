# Q. write a python programe to check weather the given array is either subsequence or subset.


n=[2,5,7,9,1]
i=0
j=1
flag=""
def function(i,j):
    global flag
    if(j>len(n)-1):
        return flag
    elif(n[i]<n[j]):
        flag="It is a subsequence"
        return function(i+1, j+1)
    else:
        flag="It is a subset"
        return flag
print(function(i,j))
