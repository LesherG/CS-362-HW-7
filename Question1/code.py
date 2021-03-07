
def fizz_buzz(num1, num2):
    ret = ""
    for i in range(num1, num2+1):
        ret += str(i)
        if(i != num2):
            ret += ", "
            
    return(ret)