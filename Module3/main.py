#conditionals
age = 18
if age>= 18:
    print('You can vote')
else:
    print('You cant vote')

age_zoo = 12

if age_zoo<=7:
    print('You can go for free')
elif 7<= age_zoo <= 15:
    print("You need to pay 50% of the ticket")
else:
    print("You need to pay the whole ticket")

#nestle conditionals
student_gpa = 4.0
student_score = 55

if student_gpa>= 3.5:
    if 50<= student_score <= 65:
        print(f"Student with a GPA of {student_gpa} and a score of {student_score} is eligible for a partial scholarship")
    elif student_score>65:
        print(f"Student with a GPA of {student_gpa} and a score of a {student_score} is eligible for a full scholarship")
    else:
        print("Student cannot get a scholarship")
else:
    print("Student cannot get a scholarship")

#set
my_set = {1, 2, 3}

my_set.remove(3)
my_set.discard(8)


len(my_set)
length_set = len(my_set)
print(length_set)

