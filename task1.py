def calculateGPA(m, ch, en, m_credit, ch_credit, en_credit):
    print("\nYour overall GPA: ")
    gpa = m * m_credit + ch * ch_credit + en * en_credit
    gpa = gpa / (m_credit + ch_credit + en_credit)

    if 0.7 < gpa < 1.0:
        gpa = 1
    elif 1.0 < gpa < 1.3:
        gpa = 1.3
    elif 1.3 < gpa < 1.7:
        gpa = 1.7
    elif 1.7 < gpa < 2.0:
        gpa = 2.0
    elif 2.0 < gpa < 2.3:
        gpa = 2.3
    elif 2.3 < gpa < 2.7:
        gpa = 2.7
    elif 2.7 < gpa < 3.0:
        gpa = 3.0
    elif 3.0 < gpa < 3.3:
        gpa = 3.3
    elif 3.3 < gpa < 3.7:
        gpa = 3.7
    elif 3.7 < gpa < 4.0:
        gpa = 4.0
    elif 4.0 < gpa < 4.3:
        gpa = 4.3
    if 0 < gpa < 4.3:
        print(gpa)
    else:
        print('Error')


def translateLetter(*letters):
    gpa_points = []
    for letter in letters:
        if letter == 'A+':
            gpa_points.append(4.3)
        elif letter == 'A':
            gpa_points.append(4.0)
        elif letter == 'A-':
            gpa_points.append(3.7)
        elif letter == 'B+':
            gpa_points.append(3.3)
        elif letter == 'B':
            gpa_points.append(3.0)
        elif letter == 'B-':
            gpa_points.append(2.7)
        elif letter == 'C+':
            gpa_points.append(2.3)
        elif letter == 'C':
            gpa_points.append(2.0)
        elif letter == 'C-':
            gpa_points.append(1.7)
        elif letter == 'D+':
            gpa_points.append(1.3)
        elif letter == 'D':
            gpa_points.append(1.0)
        elif letter == 'D-':
            gpa_points.append(0.7)
    print("\nYour GPA points: ")
    print(gpa_points)


def translatePercentage(*percentages):
    points = []
    for percentage in percentages:
        if 95 <= percentage <= 100:
            points.append(4.3)
        elif 90 <= percentage <= 94:
            points.append(4.0)
        elif 85 <= percentage <= 89:
            points.append(3.7)
        elif 80 <= percentage <= 84:
            points.append(3.3)
        elif 75 <= percentage <= 79:
            points.append(3.0)
        elif 70 <= percentage <= 74:
            points.append(2.7)
        elif 65 <= percentage <= 69:
            points.append(2.3)
        elif 60 <= percentage <= 64:
            points.append(2.0)
        elif 55 <= percentage <= 59:
            points.append(1.7)
        elif 50 <= percentage <= 54:
            points.append(1.3)
        elif 45 <= percentage <= 49:
            points.append(1.0)
        elif 40 <= percentage <= 44:
            points.append(0.7)
    print("\nTranslated Letters:")
    print(points)


calculateGPA(3.3, 2.7, 4,
             4, 3, 4)
translateLetter('A+', 'B', 'C')
translatePercentage(100, 45, 55, 89)


