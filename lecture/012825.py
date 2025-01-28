'''
RECURSION 

recursion is when a function contains a call to itself.
recursive solutions are useful when the result is dependent 
on the result ofSUB-PARTS of the problem

THREE LAWS OF RECURSION

must have a base case
must change its state and move towards the base case
must call itself recursively

common example : factorial

def f(n):
    if n == 1:
        return n
    return f(n-1) * n

print(f(3))
'''

'''
Call Stack
First in, Last Out
'''

'''

set up data structures

alg1 = list
alg2 = dictionary

alg1 is way slower because it is first in, last out (FILO)
alg2 is way faster because it is a hash function/map/table
'''