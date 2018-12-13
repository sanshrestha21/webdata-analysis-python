def get_percentage(percentage):

    grade=""

    if percentage >=80:
        grade = "Distinction"
    elif percentage <80 and percentage>=60:
        grade ="First Divison"
    elif percentage <60 and percentage>=45:
        grade ="Second Division"
    elif percentage <45 and percentage>=35:
        grade ="Third Division"
    else:
        grade = "Fail"
    return grade
percentage=input("Enter ur percentage")

print get_percentage(percentage)    