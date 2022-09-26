import re
from tokenize import Double


add = lambda x, y : x + y
add(4,5)

(lambda x, y : x * y)(4,5)

def double(x):
    return x*2

seq = [1,2,3,4]
doubled = map(double ,seq)
for i in doubled:
    print(i)

doubled_lam = [(lambda x: x*2)(x) for x in seq]
doubled_lam
doubled_lam_map = list(map(lambda x: x*2,seq))
doubled_lam_map


#dict comprehension

#Exercise
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {"name":"Jose", "school":"Computing", "grades":(66, 77, 88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data["grades"]
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    tot_grade=count=0
    for i in student_list:
        tot_grade+=sum(i['grades'])
        count+=1
    return (tot_grade/len(student_list[0]['grades']))/count