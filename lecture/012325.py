import time

def f1(n):
    l = []
    for i in range(n):
        l.insert(0, i)
    return

def f2(n):
    l = []
    for i in range(n):
        l.append(i)
    return

print("f1")
start = time.time()
f1(200000)
end = time.time()
print("time elapsed: ", end - start, "sec")

print("f2")
start = time.time()
f2(200000)
end = time.time()
print("time elapsed: ", end - start, "sec")


'''
Asymptotic Behavior

    we want to analyze approx. how fast an alg. runs when 
    the size of the input approaches infinity.


Order of Magnitude Function (Big-O)

    we want to look at the worse-case / most expensive
    scenario when analyzing our alg.

    we can express the highest-order of magnitude of a 
    time funciton by dropping all lower-order terms,
    constands, and coefficients.


    
'''



'''
class A(Exception):
    pass

class B(A):
    pass

class C(Exception):
    pass

try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise B()

except A:
    print("Caught A.")

except B:
    print("Caught B.")

except C:
    print("Caught C.")

print("Resuming execution.")
'''
