#Rivers: Create a dictionary with three large rivers
#and the countries each river flows through. One
#possible key-value pair is 'nile': 'egypt'.
#* Use a loop to display a message mentioning a river
#and a country - for example:
#"The Nile runs through Egypt."
#* Use a loop to output the name of each river
#included in the dictionary.
#* Use a loop to output the name of each country
#included in the dictionary.

#Реки: создайте словарь с тремя большими реками и
#странами, по которым протекает каждая река. Одна
#из возможных пар «ключ—значение» — 'nile': 'egypt'.
#* Используйте цикл для вывода сообщения с упоминанием
#реки и страны — например:
#«The Nile runs through Egypt.»
#* Используйте цикл для вывода названия каждой реки,
#включенной в словарь.
#* Используйте цикл для вывода названия каждой страны,
#включенной в словарь.

rivers={'nile': 'egypt',
        'amazon': "peru",
        'Yangtze': "china"}

for i in rivers.keys():
    print('The '+i.title()+' runs through '+rivers.get(i).title())

print('\nIn dictionary we have this rivers: ', end='')
for i in rivers.keys():
    print(i.title(), end=' ')

print('\n\nIn dictionary we have this countries: ', end='')
for i in rivers.values():
    print(i.title(), end=' ')
