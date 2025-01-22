class Student:
    '''Student class type that contains student values'''

    def __init__(self, name=None, perm=None):
        self.name = name
        self.perm = perm
        
    #setter method
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("Student name: {}, perm: {}".format(self.name, self.perm))

    def __eq__(self, rhs):
        return self.perm == rhs.perm

    def __str__(self):
        return "Student name: {}, perm: {}".format(self.name, self.perm)

    def __add__(self, rhs):
        return [self.name, rhs.perm, rhs.name, self.perm]

    def __le__(self, rhs):
        return self.name.upper() <= rhs.name.upper()

    def __ge__(self, rhs):
        return self.name.upper() >= rhs.name.upper()

s1 = Student("Jason", 1234567)
s2 = Student("Jake", 7654321)
print(s1 <= s2)

#s = Student()
#s = Student("Jason Bui", "A284U22")
#s.setName("Jason Bui")
#s.setPerm("A284U22")
#s.printAttributes()
    
#s1 = Student("Jason", 1234567)
#s2 = Student("Joe", 7654321)
#s3 = Student("Jill", 5555555)

#studentList = [s1, s2, s3]

#for s in studentList:
#    s.printAttributes()


#s1 = Student()
#assert s1.name == None
#assert s1.perm == None

'''
Python allows us to check for equality using the == operator for our objects
By default, Python uses the memory address to determine if two objects
are the same. This is called SHALLOW EQUALITY.
'''
'''
s1 = Student("Jason", 1234567)
s2 = Student("Jason", 1234567)
print(s1)
print(s2)
print(s1 == s2)
'''
'''
Syntax Error: no code executes
Runtime Error: logic error, runs but something goes wrong during execution
Exceptions are errors that occur during program execution.
There are ways to recover from runtime errors since
we can handle exceptions in our code.

Handling Exceptions:
There general rule of exception handling is if an exception was
raised in a program and nobody catches the exception, then the
program will terminate. But we can handle exception messages
with a general structure referred to as a try / except mechanism.
'''

'''while True:
    try:
        x = int(input("Enter an int: "))
        print(x/0)
        break
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception:
        print("Input was not an int")
    print("Let's try again")
                 
print("Resuming execution")
'''
'''
Flow of execution is:
everthing within a try block is executed normally.
if an exeception occurs in the try block, execution halts and an exception message is passed to a corresponding except block.
the except block tries to catch a certain exception type.
if there is a matching type, then only the first matching except block is executed.
once done, program execution resumes past the except blocks.
'''
'''
def divide(num, denom):
    print("calling divide function")
    if denom == 0:
        raise ZeroDivisionError()
    print("returning num / denom")
    return num / denom
try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2))
except ZeroDivisionError:
    print("Error: cannot divide by zero.")

print("Resuming execution")


'''

'''
Complete Test:
testing every possible path through the code in every possible situation

Unit Testing:
testing individual pieces of a program to ensure correct behavior

Test Driven Development:
1. write test cases that describe what the intended behavior of a unit of software should be
2. implement the detials of the functionality with the intention of passing the test
3. repeat until the tests pass
''' 

def biggestInt(a, b, c, d):
    biggest = 0
    if a >= b and a >= c and a >= d:
        return a
    if b >= a and b >= c and b >= d:
        return b
    if c>= a and c >= b and c >= d:
        return c
    return d

def test_biggestInt1():
    assert biggestInt(1,2,3,4) == 4
    assert biggestInt(1,2,4,3) == 4
    assert biggestInt(2,4,1,3) == 4

def test_biggestInt2():
    assert biggestInt(5,5,5,5) == 5

def test_biggestInt3():
    assert biggestInt(-5,-3,-12,-99) == -3


'''

Inheritance is a way of extending the functionality and properties of an existing class
allows us to add new and replace existing features

'''