# write a python program to check whether the given array is subarray or not using recursion.

n=[2,3,4,5,6,7]
i=0
j=1
flag=""
def func(i,j):
    global flag
    if(j>=len(n)-1):
        return flag
    s=n[i]+1
    if(s==n[j]):
        flag="it is a  subarray....."
        return func(i+1,j+1)
    else:
        flag="It is not a subarray"
        return flag

print(func(i,j))
