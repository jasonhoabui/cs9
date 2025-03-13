from Event import Event
from CourseCatalog import CourseCatalog
from CourseCatalogNode import CourseCatalogNode

def test_CourseCatalog_removeSection():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    sections = [section1, section2]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    assert cc.removeSection("cmpsc", 9, section1) == True
    assert section1 not in cc._getCourse("cmpsc", 9, cc.root).sections

    non_existent_section = Event("W", (1600, 1650), "north hall 1109")
    assert cc.removeSection("cmpsc", 9, non_existent_section) == False

    assert cc.removeSection("cmpsc", 10, section2) == False

def test_CourseCatalog_removeCourse():
    cc = CourseCatalog()

    lecture1 = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    sections1 = [section1]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture1, sections1)

    lecture2 = Event("TR", (1300, 1550), "arts 2628")
    sections2 = []
    cc.addCourse("art", 10, "introduction to painting", lecture2, sections2)

    lecture3 = Event("MWF", (900, 950), "engineering 101")
    sections3 = []
    cc.addCourse("engr", 5, "introduction to engineering", lecture3, sections3)

    assert cc.removeCourse("art", 10) == True
    assert cc._getCourse("art", 10, cc.root) is None

    lecture4 = Event("MWF", (1000, 1050), "engineering 102")
    sections4 = []
    cc.addCourse("engr", 6, "advanced engineering", lecture4, sections4)
    assert cc.removeCourse("cmpsc", 9) == True
    assert cc._getCourse("cmpsc", 9, cc.root) is None

    lecture5 = Event("MWF", (1100, 1150), "engineering 103")
    sections5 = []
    cc.addCourse("engr", 4, "basic engineering", lecture5, sections5)
    assert cc.removeCourse("engr", 5) == True
    assert cc._getCourse("engr", 5, cc.root) is None

    assert cc.inOrder() == \
"""\
ENGR 4: BASIC ENGINEERING
 * Lecture: MWF 11:00 - 11:50, ENGINEERING 103
ENGR 6: ADVANCED ENGINEERING
 * Lecture: MWF 10:00 - 10:50, ENGINEERING 102
"""