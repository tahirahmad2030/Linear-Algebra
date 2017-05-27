
# Odd even sequence addition(maximum addition of subsequence). 
'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''
# odd even 
import numpy as np
def first_element(num):
    if num % 2 == 0:
       return -1;
    else:
       return 1;

def even_odd(num):
    if num%2 == 0:
        return -1;
    else:
        return 1;

def get_big_of_min_sequences(elements,i):
    print elements , i
    elements = elements[i:]
    print elements
    flag = first_element(elements[0])
    print flag
    arr=[]
    seq = i
    for j in elements:
        value = even_odd(int(j))
        if value == flag:
           seq = seq+1
           arr.append(int(j))
           continue
        else:
           return np.amax(arr),seq
    return np.amax(arr),seq      
 
elements = [3,2,4,22,3,2,5]
add=0
flag = first_element(elements[0])
seq = 0
print len(elements)
for i in range(len(elements)):
    if i < seq:
       print seq
       continue
    if i < len(elements):
       big,seq = get_big_of_min_sequences(elements,i)
    add = add + big
print add    
