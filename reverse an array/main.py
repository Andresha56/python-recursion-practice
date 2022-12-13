# write a python programe to reverse an array using recursion

array=[5,4,7,8,0,4,6,3,9,8]
t=0
i=0
j=(len(array)-1)
def reverse_array(i,j):
    if(i>=j):
        return array
    t=array[i]
    array[i]=array[j]
    array[j]=t
    return reverse_array(i+1,j-1)
result=reverse_array(i,j)
print(result)
