from Event import Event

class CourseCatalogNode:

    def __init__(self, department, courseId, courseName, lecture, sections):
        self.department = department.upper()
        self.courseId = int(courseId)
        self.courseName = courseName.upper()
        self.lecture = lecture
        self.sections = sections
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        res = f'{self.department} {self.courseId}: {self.courseName}\n'
        res += f' * Lecture: {self.lecture}\n'
        for section in self.sections:
            res += f" + Section: {section}\n"
        return res