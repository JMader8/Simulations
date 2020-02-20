import random

def bubble_sort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
    
    for i in range(n):
        for j in range(0, n-i-1):
            a = arr[j]
            b = arr[j+1]

            aface  = a[0:len(a)-1];
            asuit  = a[len(a)-1];
            avalue = f[aface] if aface in f else int(aface)

            bface  = b[0:len(b)-1];
            bsuit  = b[len(b)-1];
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit or (asuit == bsuit and avalue > bvalue)):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

###

cards = deal()
print("Before shuffle: ")
print(cards)

shuffle(cards)
print("After shuffle: ")
print(cards)

bubble_sort(cards)
print("After bubble sort: ")
print(cards)

import sys 
A = cards
s={"♠":0,"♥":1,"♦":2,"♣":3}
f={"A":1,"J":11,"Q":12,"K":13}
  
# Traverse through all array elements 
for i in range(len(A)): 


    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j

            a              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("After selection sort") 
for i in range(len(A)): 
    print("%d" %A[i]),

