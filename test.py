from Markbook import Student, Course

def test1():
    """
    Ensure that you can add a Course
    """
    John = Student({'firstname': 'John', 'lastname': 'jinglehiemer'})
    John.addCourse('Math')
    John.printCourses()
    del John
    try:
        John.printClasses()
    except NameError:
        print('passed')

def test2():
    """
    Ensure that the name must be a dict
    """
    try:
        John = Student('John')
    except AssertionError:
        print('passed')

def test3():
    """
    Test Course Functions
    """
    testCourse = Course('Test')
    testCourse.addUnit(1, 'TestCourse1')
    testCourse.addUnit(2, 'TestCourse2')
    testCourse.addUnit(3, 'TestCourse3')

    testCourse.printUnits()

    testCourse.setWeight('equal')

    testCourse.printWeights()

    
tests = {
    '1' : test1,
    '2' : test2,
    '3' : test3
}

if __name__ == '__main__':
    ui = ''
    while ui != 'exit':
        
        try:
            ui = input('Which test would you like to run? (' + min(tests.keys()) + ' - ' + max(tests.keys()) + ')')
            if ui == 'exit':
                continue
            if ui == 'all':
                for test in tests.values():
                    try:
                        test()
                    except:
                        continue
            elif int(ui) in range(int(min(tests.keys())), int(max(tests.keys())) + 1):
                print('\n-------------------------------------')
                print('test: ', ui)
                tests[ui]()
                print()
        except ValueError: # if ui cannot be converted into an int
            print('enter a valid number or "exit"')
            continue
            
