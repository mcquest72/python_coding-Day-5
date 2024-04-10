
'''This program calculates the average students height from a list of heights'''

print()
student_heights = input('Input a list of student heights ').split()
print()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)
print()

# using sum and len function
# print(sum(student_heights))
# print(len(student_heights))
# print()

# print(round(sum(student_heights) / len(student_heights)))
# print()

# using for loop
total_heights = 0
for heights in student_heights:
    total_heights += heights
print(total_heights)

number_of_students = 0
for ln in student_heights:
    number_of_students += 1
print(number_of_students)

average_heights = round(total_heights / number_of_students)
print(average_heights)
print()