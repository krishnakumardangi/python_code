#This is parabola function which produce curvature like horizontal parabola.
def parabola(n,r):
    
    if(r>0):                                #This to check sign of r, so that we can decide its nature.
        N=int(n/2)
        if(n%2==0):                         #To check n is odd or even, it help help us to decide in symmetric nature.
            n=int(n/2)
            g=n-2*n
        else:
            n=int(n/2)
            g=n-2*n
            n=n+1

        for i in range(g,n,1):               #Here, start x coordinate of parabola
            s=' '
            f=(i)*(i)*(r)                    #This is equation of horizontal parabola.
            for j in range(int(f)):          #This for loop is to create space (s=str()) accornding to our need.
                s=s+' '
            print(s,end='')                  #To print s space.
            print('*')                       #To print '*' after s space.
    else:
        r=r-2*r
        N=int(n/2)
        if(n%2==0):                          #To check n is odd or even, it help help us to decide in symmetric nature.
            n=int(n/2)
            g=n-2*n
        else:
            n=int(n/2)
            g=n-2*n
            n=n+1

        for i in range(g,n,1):                #Here, start x coordinate of parabola.               
            s=' '
            f=N*N*r-(i)*(i)*(r)+1/2               #This is equation of horizontal parabola but in opposite direction.
            for j in range(int(f)):           #This for loop is to create space (s=str()) accornding to our need.
                s=s+' '
            print(s,end='')                   #To print s space.
            print('*')                        #To print '*' after s space.
            
print("Enter number of lines and curvature")
n=int(input())                                #It is number of line in curvature.
r=float(input())                              #It is degree/direction of curvature.
parabola(n,r)                                 #Here, we call our function parabola.

