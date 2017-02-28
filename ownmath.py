# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:30:14 2016

@author: gabor
"""
import math as math


def primefinder(prime):
    """finds out wheter if a number is prime if it is returns true"""
    sqroot=int(math.ceil(math.sqrt(prime)))+1
   # print "this is the squre root " + str(sqroot)
    for i in range(2,sqroot):
        #print i
        if prime % i == 0:
            return False
    return True
    
    
   #test cases fo this shit if it works IT WORKS 
"""for k in range(150):
    
    print(str(k)+ " is a prime?" +str(primefinder(k)))
     
  """  
def numerals(num):
      """gets a number returns its numerals in REVERSE order(needs fix or antoher function)"""
      tens = 10
      retlist = []
      while(num> 0):
          a = (num % tens)
          a = a/(tens/10)
          retlist.append(a)
          num = num-(a*(tens/10))
          tens = tens*10
      
      return retlist
     
print(numerals(3123124124))

def euclidian_divisor(firstnum,secondnum):
     """gets two numbers and returns their greatest common divisor very fast"""
     if(firstnum > secondnum):
        divide = firstnum
        divisor = secondnum
     else:
        divide = secondnum
        divisor = firstnum
     while(divisor != 0):
          divisor2 = divisor
          divisor = divide % divisor
          divide = divisor2
          print(divide,divisor,divisor2)
     return divide
    
print (euclidian_divisor(6,9))

