Mikhail_information={'weight': '70kg',
                     'salary': 1618,
                     'car_availability': False,
                     'home_availability': True,
                     'hobbies': ['reading', 'chatting', 'watching football', 'playing computer games'],
                     'growth': 1.82}
for i in Mikhail_information.keys():
    print('We have information about Mikhail '+str(i)+'.')
    temp=Mikhail_information[i]
    if type(temp) is list:
        print('In the base it is: ', ', '.join(temp), '.', sep='')
    else:
        print('In the base it is: '+str(temp)+'.')
