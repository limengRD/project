L = [1,2,3,4,5]
def prime(n):
    if n % 2 == 0:
        return True    
    else:
        return False
a = list(filter(prime,L))
print(a)
 
