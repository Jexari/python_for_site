'''8 Привилегии. Напишите класс с именем Privileges,
который имеет только один атрибут - привилегии, в
котором хранится список строк, упомянутых в упражнении
7. Переместите в этот класс метод show_privileges ().
В классе Admin в качестве атрибута используется
экземпляр Privileges. Создайте экземпляр Admin и
используйте метод show_privileges () для отображения
его привилегий.'''

'''8 Privileges. Write a class called Privileges that
has only one attribute, privileges, that holds the
list of strings mentioned in Exercise 7. Move the
show_privileges() method to this class. The Admin
class uses an instance of Privileges as an attribute.
Create an instance of Admin and use the show_privileges()
method to display its privileges.'''

class Privileges():
    def __init__(self, right):
        self.right=right
    def show_privileges(self):
        for i in range(len(self.right)):
            print(str(i)+'.', self.right[i])
        
class User():
    def __init__(self, first_name, last_name, avatar, password):
        self.first_name=first_name
        self.avatar=avatar
        self.password=password
        self.last_name=last_name
    def describe_user (self):
        print("User's first name: "+self.first_name.title()+'.')
        print("User's last name: "+self.last_name.title()+'.')
        print("User's avatar: "+self.avatar+'.')
        print("User's password: "+str(self.password)+'.')
    def greet_user (self):
        print('Hello '+self.first_name.title()+' '+self.last_name.title()+'!')

class Admin(User):
    def __init__(self, first_name, last_name, avatar, password, right):
        super().__init__(first_name, last_name, avatar, password)
        self.right=right
        print(self.first_name.title(), self.last_name.title(), 'can:')
        self.privileges=Privileges(self.right)
        self.privileges.show_privileges()

andrey=User('andrey', 'antonov', 'flowers', '2mFF04ydZo9MM6v')
andrey.describe_user()
andrey.greet_user()
print()
michael=Admin('michael', 'kuznetsov', 'car', 's2i1V1F8ue', ["add a message", "delete a message", "block user"])
michael.describe_user()
michael.greet_user()
