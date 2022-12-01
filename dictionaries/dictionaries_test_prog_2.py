students_marks={'Yen': 5,
                'Jan': 4,
                'Maria': 3,
                'Juliana': 4,
                'Victor': 2,
                'Kirill': 'was ill'}
print(students_marks.keys())
print(students_marks.values())

students_marks.pop('Kirill')
# or you cen use:    del students_marks['Kirill']


students_marks['Juliana'] = 'was ill'
print(students_marks.items())
