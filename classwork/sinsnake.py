import math,time
def sinsnake(n,amplitude):

    for i in range(n):
        
        s=' '
        f=amplitude*(math.sin(i))
        for j in range(int(f)):
            s=s+' '
        print(s+'*')

n=int(input('Input size of snake: '))
a=int(input('Input area to cover: '))
sinsnake(n,a)

