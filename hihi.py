# a program to find a factorial 
n = int(input('enter the number of which you want to print a factorial '))
if n == 0 and n == 1:
    print(1)
elif n > 0 :
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
        i +=1
    print(fact)
else :
    print("please enter a valid number ")
    
        
        