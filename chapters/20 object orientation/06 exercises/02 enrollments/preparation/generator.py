import sys
import datetime
import importlib
from test_utils import *

# set fixed seed for generating test cases
random.seed(123456789)

# exercise directories
evaldir = create_dir('..', 'evaluation')         # evaluation
solutiondir = create_dir('..', 'solution')       # solution

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.en.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

for name in dir(module):
    if not (name.startswith('__') and name.endswith('__')):
        globals()[name] = eval(f'module.{name}')

# generate test data for classes Course and Student
courses = [
    (238273, 'Astronomy'),
    (983448, 'Charms'),
    (746473, 'Dark Arts'),
    (462763, 'Defence Against Dark Arts'),
]
students = [
    (29839339, 'Harry', 'Potter', datetime.date(1980, 7, 31)),
    (24837367, 'Hermione', 'Granger', datetime.date(1979, 9, 19)),
    (27373378, 'Ron', 'Weasley', datetime.date(1980, 3, 1)),
]

# generate unit tests for class Course
sys.stdout = open(os.path.join('..', 'evaluation', '0.in'), 'w', encoding='utf-8')
for index, course in enumerate(courses):

    # instantiation
    varname = course[1].lower().replace(' ', '_')
    obj = test_instantiation(Course, *course, varname=varname)

    # test string conversion (str)
    tests = ['repr', 'str']
    if index:
        random.shuffle(tests)

    for test in tests:

        if test == 'repr':
            test_repr(obj, varname=varname, call=None if index else False)
        elif test == 'str':
            test_str(obj, varname=varname, call=None if index else False)

    print()

# generate unit tests for class Student
sys.stdout = open(os.path.join('..', 'evaluation', '1.in'), 'w', encoding='utf-8')
for index, student in enumerate(students):

    try:

        # instantiation
        print('>>> import datetime')
        varname = student[1].lower().replace(' ', '_')
        obj = test_instantiation(Student, *student, varname=varname)

        # test string conversion (str)
        tests = ['repr', 'str', 'age', 'courses']
        if index:
            random.shuffle(tests)

        for test in tests:

            if test == 'repr':
                test_repr(obj, varname=varname, call=None if index else False)
            elif test == 'str':
                test_str(obj, varname=varname, call=None if index else False)
            else:
                processor = None
                if test == 'age':
                    processor = ''
                    if not index:
                        processor += '<DEFINITION>\n'
                        with open('ageChecker.py') as checker:
                            processor += checker.read().rstrip() + '\n'
                        processor += '</DEFINITION>\n'
                    processor += '<OUTPUTPROCESSOR>\n'
                    processor += f'AgeChecker({obj.birthdate.day}, {obj.birthdate.month}, {obj.birthdate.year})\n'
                    processor += '</OUTPUTPROCESSOR>\n'
                test_method(obj, test, varname=varname, processor=processor)

    except Exception as e:
        print('Traceback (most recent call last):\n{}: {}'.format(e.__class__.__name__, e))

    print()

# generate unit tests for class Student
sys.stdout = open(os.path.join('..', 'evaluation', '2.in'), 'w', encoding='utf-8')
print('>>> import datetime')

course_dict = {}
for course in courses:
    varname = course[1].lower().replace(' ', '_')
    obj = test_instantiation(Course, *course, varname=varname, newcontext=False)
    course_dict[varname] = obj

student_dict = {}
for student in students:
    varname = student[1].lower().replace(' ', '_')
    obj = test_instantiation(Student, *student, varname=varname, newcontext=False)
    student_dict[varname] = obj

for _ in range(20):

    student_name, student = random.choice(list(student_dict.items()))
    r = 1 if random.random() < 0.8 else 2
    enrollments = random.sample(list(course_dict.items()), r)

    # generate test statement
    statement = f'>>> {student_name}'
    for course_name, course in enrollments:
        statement += f'.enroll({course_name})'
        student.enroll(course)
    statement += '.courses()'
    print(statement)

    # generate test result
    print(f'{student_dict[student_name].courses()!r}')
