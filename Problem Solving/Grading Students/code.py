def gradingStudents(grades):
    # Write your code here
    l1 = []
    for grade in grades:
        x = (int(grade/5) + 1) * 5
        y = x - grade
        if grade < 38:
            l1.append(grade)
        elif y < 3:
            l1.append(x)
        else:
            l1.append(grade)
    
    return l1
