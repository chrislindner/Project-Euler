# prime.py
# Problem 3 from Project Euler.
# Finds the largest prime factor of a number.
# INPUTS: None (number is set as "target" below)
# OUTPUTS: The code searches for prime factors of the target number
#          then divides the number by the prime factor as it finds them and
#          stars the search again.  It will output its progress as it finds
#          prime factors and give the largest prime factor at the end.

# function bool isprime(int number)
# Uses a brute force check to determine if a number is prime.
# Returns 1 if the number is prime, 0 if it is not.
# No input error handling.
def isprime(number):
    prime = 1
    for i in range (2,prime):
        if number % i == 0:
            prime = 0
            break
    
    return prime
    
    
if __name__ == "__main__":
    target = 600851475143
    
    i = 2
    while i < target:
        if isprime(i):
            if target % i == 0:
                print "Target " + str(target) + " has prime factor " + str(i) + ". New target: " + str(target/i)
                target = target / i
                i = 1

        
        i = i + 1
                
                
                
    print "\n" + str(target) + " is the largest prime factor."
    