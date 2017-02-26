import math

def sieve(maxi):
    """implementation of the sieve of erathosthenes
    crosses out every non prime number ,based on the pseudocode from wikipedia"""
    bool_list = []
    for i in range(0,maxi):
        bool_list.append(True)
    for i in range(2,int(math.ceil(math.sqrt(maxi)))):
        if ( bool_list[i] == True ):
            j = i*i
            print(i,"value of i")
            while(j <= maxi-1):
                print(j,"value of j")
                bool_list[j] = False
                j = j+i 
    intbool_list = []
    bool_list[0] = False
    bool_list[1] = False
    for i in range(maxi):
         if(bool_list[i] == True):
             intbool_list.append(i)
         #changes the booleans into more human readable integers
    
    return intbool_list
    
print(sieve(14))
    


        
        
