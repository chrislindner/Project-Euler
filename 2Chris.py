# fib.py
# Problem 2 from Project Euler
# Calculates the sum of the even Fibonacci Numbers below four million
# INPUTS: None (parameters set below)
# OUTPUTS: The sum.

if __name__ == "__main__":
    maxval = 4000000
    
    old = 1
    new = 2
    sum = 0
    
    while new < maxval:
        if new % 2 == 0:
            sum = sum + new
        
        lastnew = new
        new = old + new
        old = lastnew
            
    print "The sum of the even Fibonacci Numbers below " + str(maxval) + " is " + str(sum)
    
    
    