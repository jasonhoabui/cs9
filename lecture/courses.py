#from [filename without .py] import [component]
from student import Student

s = Student()

class Courses:
    ''' Class represents a collection of courses. Courses are organized with
        a dictionary where the key is the course number, and the value
        is a list of students in a course '''


    def __init__(self):
        self.courses = {}

    def addStudent(self, student, courseNum):
        ''' Method that adds a student object to a courseNum '''
        # If the course doesn't exist
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]

        elif not student in self.courses.get(courseNum):
            self.courses[courseNum].append(student)



    def printCourses(self):
        ''' Print out everything '''
        for courseNum in self.courses:
            print("CourseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
                
'''
s1 = Student("Jason", 1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 5555555)

UCSB = Courses()
UCSB.addStudent(s1, "CS8")
UCSB.addStudent(s2, "CS9")
UCSB.addStudent(s3, "ENGR3")
UCSB.addStudent(s3, "CS8")

UCSB.printCourses()
'''

s1 = Student("Gaucho", 1234567)
UCSB = Courses()
UCSB.addStudent(s1, "CS9")
courses = UCSB.courses
assert courses == {"CS9": [s1]}
