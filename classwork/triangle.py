def isoscelse_triange(n):
    
    #s=int(n/2+1)
    #print(s)
    for i in range(n):
        for k in range(n-i+1):
            print(" ",end="")
        for j in range(2*i+1):
            print('*',end='')
        print("")

def isoscelse_op_triange(n):
    n=2*n
    #s=int(n/2+1)
    #print(s)
    
    for i in range(n):
        print(' ',end='')
        for k in range(i+1):
            print(" ",end="")
        for j in range(n-2*i-1):
            print('*',end='')
        print("")

def long_triangle(n):
    for i in range(n):
        for k in range(4):
            for k in range(n-i+1):
                print(" ",end="")
            for j in range(2*i+1):
                print('*',end='')
            print('')


'''def both_long_triangle(n):
    for i in range(n):
        for k in range(4):
            for h in range(i+1):
                print(" ",end="")
            for j in range(2*n-2*i+1):
                print('*',end='')
            print('')'''

def both_long_triangle(n):
    for i in range(n):
        for k in range(4):
            for k in range(i+2):
                print(" ",end="")
            for j in range(2*n-2*i-1):
                print('*',end='')
            print('')
    


        

print('Your are fond of triangle and star symbols. Bingo, you are at right place.')
#n=int(input('Enter a number: '))
#l=int(input('Choose a number (from 1-4): '))
flag=1
while(flag!=0):
    n=int(input('Enter a number: '))
    l=int(input('Choose a number (from 1-4): '))
    if(l==2):
        isoscelse_triange(n)
        isoscelse_op_triange(n)
    elif(l==1):
        isoscelse_triange(n)
    elif(l==3):
        long_triangle(n)
    elif(l==4):
        long_triangle(n)
        both_long_triangle(n)
    else:
        print('Hey, first choose a number....')
    d=str(input('You want to try more(y/n): '))
    if(d=='n'):
       flag=0
    else:
        flag=1        
                
