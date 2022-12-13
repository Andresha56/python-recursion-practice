a=["M","A","D","A","M"]

i=0
j=len(a)-1
def reverse_str(i,j):
    if i>=j:
        return (f"It is a palendron\n{a}")
    elif(a[i]==a[j]):
        t=a[i] 
        a[i]=a[j]
        a[j]=t
        return reverse_str(i+1,j-1)
    else:
        return ("It is not a palendron")
print(reverse_str(i,j))
