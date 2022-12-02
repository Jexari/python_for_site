#Favorite numbers: Use a dictionary to store your
#favorite numbers. Take five names and use them as
#dictionary keys. Come up with a favorite number for
#each person and save it as a value in a dictionary.
#Print the name of each person and their favorite number.

#Любимые числа: Используйте словарь для хранения
#любимых чисел. Возьмите пять имен и используйте их
#как ключи словаря. Придумайте любимое число для
#каждого человека и сохраните его как значение в
#словаре. Выведите имя каждого человека и его любимое число.

favourite_numbers={'David': 51,
                   'Ian': 1,
                   'Maria': 2,
                   'Ivan': 10,
                   'Ilya': 15}
for i in favourite_numbers.keys():
    print(i+"'s favourite number: "+str(favourite_numbers[i])+".")
