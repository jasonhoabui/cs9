from Event import Event
from CourseCatalogNode import CourseCatalogNode

class CourseCatalog:

    def __init__(self):
        self.root = None
    
    def addCourse(self, department, courseId, courseName, lecture, sections):
        if self._getCourse(department.upper(), courseId, self.root) is not None:
            return False
        if not self.root:
            self.root = CourseCatalogNode(department, courseId, courseName, lecture, sections)
        else:
            self._addCourse(department, courseId, courseName, lecture, sections, self.root)
        return True

    def _addCourse(self, department, courseId, courseName, lecture, sections, currentNode):
        department = department.upper()
        if department < currentNode.department or (department == currentNode.department and courseId < currentNode.courseId):
            if currentNode.left:
                self._addCourse(department, courseId, courseName, lecture, sections, currentNode.left)
            else:
                currentNode.left = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                currentNode.left.parent = currentNode
        else:
            if currentNode.right:
                self._addCourse(department, courseId, courseName, lecture, sections, currentNode.right)
            else:
                currentNode.right = CourseCatalogNode(department, courseId, courseName, lecture, sections)
                currentNode.right.parent = currentNode
    
    def _getCourse(self, department, courseId, currentNode):
        department = department.upper()
        if not currentNode:
            return None
        if department == currentNode.department and courseId == currentNode.courseId:
            return currentNode
        elif department < currentNode.department or (department == currentNode.department and courseId < currentNode.courseId):
            return self._getCourse(department, courseId, currentNode.left)
        else:
            return self._getCourse(department, courseId, currentNode.right)

    
    def addSection(self, department, courseId, section):
        courseNode = self._getCourse(department.upper(), courseId, self.root)
        if not courseNode:
            return False
        courseNode.sections.append(section)
        return True

    def inOrder(self):
        res = []
        if self.root:
            self._inOrder(self.root, res)
        return "".join(res)

    def _inOrder(self, currentNode, res):
        if currentNode:
            self._inOrder(currentNode.left, res)
            res.append(str(currentNode)) 
            self._inOrder(currentNode.right, res)


    def preOrder(self):
        res = ""
        if self.root:
            res = self._preOrder(self.root)
        return res
    
    def _preOrder(self, currentNode):
        res = ""
        if currentNode:
            res += str(currentNode)
            res += self._preOrder(currentNode.left)
            res += self._preOrder(currentNode.right)
        return res
    
    def postOrder(self):
        res = ""
        if self.root:
            res = self._postOrder(self.root)
        return res
    
    def _postOrder(self, currentNode):
        res = ""
        if currentNode:
            res += self._postOrder(currentNode.left)
            res += self._postOrder(currentNode.right)
            res += str(currentNode)
        return res

    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        courseNode = self._getCourse(department.upper(), courseId, self.root)
        if not courseNode:
            return ""
        attendableSections = ""
        for section in courseNode.sections:
            if section.day == availableDay:
                startTime, endTime = section.time
                availableStartTime, availableEndTime = availableTime
                if startTime >= availableStartTime and endTime <= availableEndTime:
                    attendableSections += f"{section}\n"
        return attendableSections

    def countCoursesByDepartment(self):
        departmentCounts = {}
        if self.root:
            self._countCoursesByDepartment(self.root, departmentCounts)
        return departmentCounts
    
    def _countCoursesByDepartment(self, currentNode, departmentCounts):
        if currentNode:
            if currentNode.department in departmentCounts:
                departmentCounts[currentNode.department] += 1
            else:
                departmentCounts[currentNode.department] = 1
            self._countCoursesByDepartment(currentNode.left, departmentCounts)
            self._countCoursesByDepartment(currentNode.right, departmentCounts)