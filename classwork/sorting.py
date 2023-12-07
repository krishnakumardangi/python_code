import random
#import time
#import math
#import pdb
#pdb.set_trace()
"""
NOTE:
    1. The header information of all the functions should contain the details of
    the code that is written under that function.
    2. Write your share of comments on every single line possible.
    3. You can include more functions to make your code more modular but the
    given functions and their names should not be changed. 
    4. There shouldn't be any print or input statements through out the code.  

    The following sort functions will take a list L as input and return 
    a sorted list by using the given sorting technique. 
    
    selection_sort(L)
    bubble_sort(L) 
    merge_sort(L) 
    bogo_sort(L)  
    quick_sort(L)
    insertion_sort(L)
   
    naive_search(x,L): You need to search for the element x in L by going through the elemnts of the list one by one. 
    binary_search(x,L): Search using the popular binary search technique. 
""" 



def selection_sort(L):          #Verified
    for i in range(len(L)):     #To itrate in given list.
        min=L[i]
        L.remove(min)           #pick one element and remove and then check
        for j in range(i,len(L),1): #Now, we will try to minimum number of this and pick that one
            if(L[j]<min):
                temp=min
                min=L[j]
                L[j]=temp
        L.insert(i,min)             #Insert minimum element at position where we pick one by assuming it is minimum
    return L                    #return sorted list

#print(selection_sort([5,6,8,5,9,2,3,1]))


def bubble_sort(L):       #Verified
    for i in range(len(L)):     #Start iterating list
        for j in range(0,len(L)-i-1,1):   #Start swaping maximum element
            if(L[j+1]<L[j]):
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp
    return L

#print(bubble_sort([5,6,8,9,2,3,5,1]))


def merge_sort(L):       #verified
    #Here first we have to merge and then sort it
    #Mearge and then sort the list
    def merge_two_sorted_list(l1,l2):      #Verified #To merge two sorted list
        new_list=[]
        while(len(l1)!=0 or len(l2)!=0):   #list must not empty
            if(len(l1)>0 and len(l2)>0):    #if both list contain element
                if(l1[0]<=l2[0]):
                    new_list.append(l1[0])
                    l1.remove(l1[0])
                else:
                    new_list.append(l2[0])
                    l2.remove(l2[0])
            else:          #if on;ly one element contain element
                if(len(l1)==0):
                    new_list.append(l2[0])
                    l2.remove(l2[0])
                else:
                    new_list.append(l1[0])
                    l1.remove(l1[0])
        return new_list
    def merge_sortl(l):      #Verified
        if(len(l)==1):
            return l     #if list contain only one element
        else:         #otherwise go for recusion
            a=merge_sortl(l[:len(l)//2])  #slice the list in two part
            b=merge_sortl(l[len(l)//2:])
            return merge_two_sorted_list(a,b)
    sorted_list=merge_sortl(L)
    return sorted_list
#L=[1,35,464,7464,11,853,65,3,74,4,631,746,4,1,3,46,63]
#print(merge_sort(L))



def bogo_sort(L):      #Verified
    flag=0
    s=len(L)-1
    while(flag!=1):
        for i in range(s):        #To check list is sorted or not.
            if(L[i]>=L[i+1]):      #To break when list not follow property of list
                break
            elif(i==len(L)-2):     #After end of list if it follow  property of list
                flag=1
                return L
        random.shuffle(L)      #Re-shuffle the list
#L1=[1,8,2,3]
#print(bogo_sort(L1))


def quick_sort(L):     #verified
    def segragation(l):     #To segragate list in required order
        a=[]
        b=l.pop(len(l)-1)     #To pivot last element
        c=[]
        for x in l:      #make list which contain element less than b
            if(x<=b):
                a.append(x)
        for x in l:      #make list which contain element greater than b
            if(x>b):
                c.append(x)
        return a,b,c
    f,m,n=segragation(L)
    if((len(f)==1 or len(f)==0)and(len(n)==1 or len(n)==0)):
        f.append(m)
        return f+n               #return list if no further segragated
    else:     #otherwise segragate it more
        if(len(f)>1):
            f=quick_sort(f)
        if(len(n)>1):
            n=quick_sort(n)
        f.append(m)
        return f+n

#List=[2,3,1,4,7,25,6,9,2,5]
#print(quick_sort(List))



def insertion_sort(L):        #Verified
    for i in range(len(L)):
        p=L[i]                #point out a element
        for j in range(i,-1,-1):
            if(p<=L[j]):            #check that element p before other element who is maximum
                if(j==0 and p<L[j]):  #check the certeria
                    L.pop(i)
                    L.insert(j,p)
                elif(p>L[j-1]):
                    L.pop(i)
                    L.insert(j,p)
    return L

#print(insertion_sort([5,6,8,9,2,3,5,45,1]))


def naive_search(x,L):        #Verified
    for i in range(len(L)):    #Start iterating in list and try to check it is avialable or not
        if(L[i]==x):    #if element found then return ture
            return 1
            break
        elif(i==len(L)-1):    #if list at its end and element not found then return false
            return 0
        else:
            pass
    return 0

#print(naive_search(196,[8,9,6,1,5,7,3,196,2,15]))

def binary_search(x,l):     #Verified
    e=len(l)-1              #To point end of list
    if(e>=0):
        mid=e//2            #To find mid/median point of list
        if(l[mid]==x):      #If we found element
            return 1
        elif(l[mid]>x):     #if element in other half of list
            return binary_search(x,l[:mid-1])     #slice the list and choose correct list
        else:
            return binary_search(x,l[mid+1:])
    else:
        return 0          #if element is not found

#L=[1,2,3,4,5,6,7,8,9]
#print(binary_search(10,L))
