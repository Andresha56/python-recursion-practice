array=[7,4,5,1,4,3,7,3,9,8,8]
s=sorted(array)
i=0
j=1
sum=0
def function(i,j):
    global sum
    if(j>=len(s)-1):
        return sum
    elif(s[i]==s[j]):
        sum+=s[i]+s[j]
        return function(i+1,j+1)
    else:
        return function(i+1,j+1)
result=function(i,j)
print(result)
