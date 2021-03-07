
def fizz_buzz(num1, num2):
    ret = ""
    for i in range(num1, num2+1):
        if(i != num1):
            ret += ", "
        if(i % 3 == 0):
            ret += 'Fizz'
            continue
        ret += str(i)
        
            
    return(ret)