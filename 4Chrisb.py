# pali.py

import time

# Problem 4 from Project Euler
# There are probably more efficient ways to do this...

def ispali(number):
    numstr = str(number)
    pali   = 1
    
    for i in range(int(len(numstr)/2)):
        if numstr[i] != numstr[-i-1]:
            pali = 0
            
    return pali


if __name__ == "__main__":   
    ts=time.time()
    
    maxprod = 0
    
    for n1 in range(9999,999,-1):
        for n2 in range(9999,999,-1):
            product = n1*n2
            if product > maxprod and ispali(product):
                maxprod = product
        
    print maxprod
       
    te=time.time()
    print 'time taken: %f'%(te-ts)  