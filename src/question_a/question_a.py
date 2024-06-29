#write functions here, don't add input('') statements here!
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt = int(num **0.5)+1
    for i in range(3,sqrt+1, 2):
        if num % i == 0:
            return False
        
    return True    
        

def test_config():
    return True


