# problem1.py
# Project Euler Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000

if __name__ == "__main__":
    target = 1000
    sum = 0
    
    for i in range (1,target):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    
    print "The sum of all multiples of 3 or 5 below " + str(target) + " is " + str(sum)