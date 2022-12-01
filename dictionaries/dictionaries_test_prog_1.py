students_marks={'Yen': 5,
                'Jan': 4,
                'Maria': 3,
                'Juliana': 4,
                'Victor': 2,
                'Kirill': 'was ill'}
print(students_marks)
print(students_marks['Maria'])
print(students_marks.get('Kirill'))

print(students_marks.get('Yan'))
#there is no error as we can see

#print(students_marks['Yan'])
#if you activate this string you will receive an error


student_who_eat_in_dining_room={}
student_who_eat_in_dining_room["Jan"] = True
student_who_eat_in_dining_room["Kirill"] = True
student_who_eat_in_dining_room['Victor'] = False
print(student_who_eat_in_dining_room)
