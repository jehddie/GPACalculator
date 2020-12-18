def collect_grades():
    """Collects courses data (name, units, grade)"""
    print('Enter quit when you\'re done entering all courses')
    while True:
        course_name = input("Enter your course name:")
        if not course_name:
            print('Course name cannot be empty')
            print('Enter quit when you\'re done entering all courses')
            continue
        if course_name.lower() == 'quit':
            break

        # Collects course's unit, makes sure it is of the right type
        while True:
            try:
                course_unit = int(input("Course unit:"))
                break
            except ValueError:
                print('Course unit must be of type integer')

        # Collects course's grade and makes sure it's a possible grade
        while True:
            course_grade = (input("Enter your grade:")).upper()
            if course_grade in grades_point:
                break
            else:
                print('Grade not contained in options')

        courses_data.append([course_name, course_unit, course_grade])
        print('--------------------NEXT-----------------------')
    return courses_data


def read_grades():
    """Reads the individual courses and grades"""
    try:
        with open(student_file + 'CoursesData', 'r') as f:
            lines = f.readlines()

            for i in range(4, len(lines)):
                fields = lines[i].strip('\n').split('|')
                courses_data.append([fields[0].strip(' '), int(fields[1].strip(' ')), fields[2].strip(' ')])

    except FileNotFoundError:
        print('Invalid file name')
        return 0
    return courses_data


def calc_grades(curr_course_data):
    """Calculates the GPA"""
    if not curr_course_data:
        return 0

    score = 0
    total_units = 0
    for course in curr_course_data:
        score += course[1] * grades_point[course[2]]
        total_units += course[1]
        # print(course[0])
    return score / total_units


def save_data():
    """Saves the data into a text file"""
    while True:
        save_data_option = (input("Would you like to save this data (yes/no) ?")).lower()

        if save_data_option == 'yes':
            student_name = input('Enter your first name:').strip(' ')
            my_file = student_name + 'CoursesData'

            with open(my_file, 'w') as my_f:
                my_f.write(student_name + '\'s courses\' data\n')
                my_f.write('Grade scale: ' + str(grade_scale) + '\n')
                print(file=my_f)
                print('WARNING!: CHANGING THE DATA BELOW MIGHT CAUSE ERRORS', file=my_f)
                print(file=my_f)
                for course in courses_data:
                    print(course[0], '|', course[1], '|', course[2], file=my_f)
            print('File saved!')
            break

        elif save_data_option == 'no':
            print('Got it. File not saved!')
            break

        else:
            print('Invalid input, please enter \'yes\' or \'no\'')


grade_scale = 5
grades_point = dict(A=5, B=4, C=3, D=2, E=1, F=0)
courses_data = []

print("---| GPA CALCULATOR |---")

while True:
    student_file = input("Enter your first name or press enter to start afresh:")
    if student_file == '':
        print('Your GPA is:', calc_grades(collect_grades()))
        save_data()
        break
    else:
        if read_grades() == 0:
            continue
        print('Your GPA is:', calc_grades(read_grades()))
        break
