from Event import Event
from CourseCatalog import CourseCatalog
from CourseCatalogNode import CourseCatalogNode

def test_Event_str():
    event = Event("TR", (1530, 1645), "td-w 1701")
    assert str(event) == "TR 15:30 - 16:45, TD-W 1701"
    event2 = Event("W", (1400, 1450), "north hall 1109")
    assert str(event2) == "W 14:00 - 14:50, NORTH HALL 1109"
    event3 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    assert str(event3) == "F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101"

def test_CourseCatalogNode_str():
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    sections = [section1, section2]
    node = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture, sections)
    assert str(node) == \
"""\
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
 + Section: W 15:00 - 15:50, NORTH HALL 1109
"""

def test_CourseCatalog_addCourse():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    sections = [section1, section2]
    assert cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections) == True
    assert cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections) == False

def test_CourseCatalog_addSection():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    section2 = Event("W", (1500, 1550), "north hall 1109")
    assert cc.addSection("cmpsc", 9, section2) == True
    assert cc.addSection("cmpsc", 10, section2) == False

def test_CourseCatalog_inOrder():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections1 = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections1)

    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections2 = []
    cc.addCourse("art", 10, "introduction to painting", lecture2, sections2)
    
    assert cc.inOrder() == \
"""\
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
"""

def test_CourseCatalog_preOrder():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections1 = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections1)

    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections2 = []
    cc.addCourse("art", 10, "introduction to painting", lecture2, sections2)

    assert cc.preOrder() == \
"""\
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
"""

def test_CourseCatalog_postOrder():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections1 = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections1)

    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections2 = []
    cc.addCourse("art", 10, "introduction to painting", lecture2, sections2)

    assert cc.postOrder() == \
"""\
ART 10: INTRODUCTION TO PAINTING
 * Lecture: TR 13:00 - 15:50, ARTS 2628
CMPSC 9: INTERMEDIATE PYTHON
 * Lecture: TR 15:30 - 16:45, TD-W 1701
 + Section: W 14:00 - 14:50, NORTH HALL 1109
"""

def test_CourseCatalog_getAttendableSections():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    sections = [section1, section2, section3]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    assert cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700)) == \
"""\
W 15:00 - 15:50, NORTH HALL 1109
W 16:00 - 16:50, NORTH HALL 1109
"""

def test_CourseCatalog_countCoursesByDepartment():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections1 = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections1)

    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections2 = []
    cc.addCourse("art", 10, "introduction to painting", lecture2, sections2)

    assert cc.countCoursesByDepartment() == {"CMPSC": 1, "ART": 1}