def fun(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    fun(list,index+1)

friuts=["Apple","Mango","banana","Kiwi","Grapes"]
fun(friuts)    
   

