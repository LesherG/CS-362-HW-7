

def leap_year(num):
    if(num % 4 == 0):
        if(num % 100 == 0):
            return False
        return True
    else:
        return False