class Markbook:
    def __init__(self):
        self.students = []
        self.courseList = []

    def addStudent(self, name):
        self.students.append(Student(name))

    def removeStudent(self, name):
        """ returns True if the student is found, otherwise returns false"""
        for i in range(len(self.students)):
            if name.values() == self.students[i].name.values():
                self.students.remove(name)
                return True
        return False


class Student:
    def __init__(self, _name):
        self.name = _name
        self.courses = {}
        try:
            assert type(self.name) != dict
        except AssertionError:
            print('Name must be a dictionary')
            del self
            raise AssertionError

    def addCourse(self, className):
        self.courses[className] = Course(className)
    
    def printCourses(self):
        for c in self.courses.values():
            print(c.name)


class Course:
    def __init__(self, name):
        self.name = name
        self.units = {}

    def addUnit(self, _id, _name):
        self.units[_name] = Unit(_id, _name)

    def printUnits(self):
        print('Units: ')
        counter = 1
        for unit in self.units.keys():
            print(str(counter) + '. ' + unit)
            counter += 1

    def setWeight(self, distribution):
        if distribution == 'equal':
            _weight = 100/len(self.units)
            for unit in self.units.values():
                unit.updateWeight(_weight)

    def printWeights(self):
        for unit in self.units.values():
            print(unit.name + "'s weight is " + str(unit.weight))


class Unit:
    """
    Every Course is going to have several units
    """
    def __init__(self, _id, _name, _weight=0):
        self.id = _id
        self.name = _name
        self.weight = _weight
        self.grade = None

    def updateGrade(self, _grade):
        self.grade = _grade

    def updateWeight(self, _weight):
        self.weight = _weight