# RECURSION===>
# Function when call itself .

def fun(n):
    if(n==8):
        return
    print(n)
    fun(n+1)
    
fun(5)

#def fun(n):
#    if(n==0 or n==1):
#        return 1
#    return fun(n-1)*n
#print(fun(5))            



