# Ques => Wap to print first natural number using recursion ?
def natural(num):
    if(num==0):
        return 0
    return natural(num-1)+num
print(natural(5))   
