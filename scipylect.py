print("hello scientific python")
def picalculator(accuracy_meter):
    """function which calculates the value of pi using the WAllis formula
    it's rather slow and I should map its approach to the Pi value in python with matplotlib
    
    """
    calculated_PI = 1.0;
    i = 1;
    while(i<accuracy_meter):
        #the wallis formula
        calculated_PI *= (4*i**2)/(4*i**2-1)
        i += 1
        
    print(calculated_PI*2)
    
def fibo_calc(lastelement):
    """this function calculates the fibonacci sequance to
    
     a given last member
     """
    fibo_list =[1,1]
    for i in range(2,lastelement):
        #u[n] = u[n-2] + u[n-1]
        #this one starts with double 1
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    print(fibo_list)
fibo_calc(40)
        
        
