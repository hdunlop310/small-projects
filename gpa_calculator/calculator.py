grades_vs_points = {'A1': 22, "A2": 21, 'A3': 20, 'A4': 19, 'A5': 18,
                    'B1': 17, 'B2': 16, 'B3': 15,
                    'C1': 14, 'C2': 13, 'C3': 12,
                    'D1': 11, 'D2': 10, 'D3': 9,
                    'E1': 8, 'E2': 7, 'E3': 6,
                    'F1': 5, 'F2': 4, 'F3': 3,
                    'G1': 2, 'G2': 1,
                    'H': 0}


def grade_validator():
    valid_grade = False
    while not valid_grade:
        print("Invalid grade must be of the form A1-5, B1-3, C1-3, D1-3, E1-3, F1-3, G1-2, H")
        grade = input('Enter your grade for course in the form A4, B3 etc...: ')
        if grade in grades_vs_points:
            valid_grade = True
    return grade


def number_validator():
    valid_number = False
    while not valid_number:
        print("Invalid entry - must be a number: ")
        try:
            number = int(input('Enter a valid number: '))
        except ValueError:
            number = number_validator()
        valid_number = True
    return number


def info(degree):
    print('\x1B[3m GPA is calculated from all the courses you have completed in your degree course. - ', degree, '\n'
          'Each grade is matched to a grade point, this is then multiplied by the credits that this course was worth \n'
          'and then divided by the total number of credits that each course was worth')
    print('ie. if you did 5 courses that were all worth 10 credits, and achieved an, \n'
          'A4, B3, C2, B1, D2, then your GPA would be: \n'
          '((22x10)+(15x10)+(13x10)+(17x10)+(10x10))/50 \n'
          ' = \033[1m 14.8 \033[0m \x1B[23m')
    print()


def gpa_calculator():
    degree = input("What is your degree subject? ")
    info(degree)
    grade_credits_dict = {}
    try:
        no_of_courses = int(input('How many ' + str(degree) + ' courses have you done over 1st and 2nd year? '))
    except ValueError:
        no_of_courses = number_validator()

    print("Now for every course you have done, you will be asked to enter the grade you achieved and how many credits "
          "that course was worth")
    for counter in range(no_of_courses):
        grade = input('Enter your grade for course in the form A4, B3 etc...: ')
        if grade not in grades_vs_points:
            grade = grade_validator(grades_vs_points)

        try:
            no_of_credits = int(input('Enter the amount of credits this course was worth: '))
            print()
        except ValueError:
            no_of_credits = number_validator()

        if grade in grade_credits_dict:
            grade_credits_dict[grade] += no_of_credits
        else:
            grade_credits_dict[grade] = no_of_credits

    grade_points = 0
    total_no_of_credits = 0

    for grade in grade_credits_dict.keys():
        grade_points += grades_vs_points[grade] * grade_credits_dict[grade]
        total_no_of_credits += grade_credits_dict[grade]

    return grade_points / total_no_of_credits


print('Your GPA is: \033[1m', gpa_calculator(), '\033[0m')
