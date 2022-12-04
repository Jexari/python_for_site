'''7 Администратор: Администратор - это особый
пользователь. Напишите класс с именем Admin и
позвольте ему наследовать класс User, который вы
написали для выполнения упражнения 3.
Добавьте атрибут, называемый привилегиями, для
хранения списка строк (например, «может добавить
сообщение», «может удалить сообщение», «может
заблокировать пользователя» и т.д.). Напишите метод
под названием show_privileges (), который отображает
права администратора. Создайте экземпляр Admin и
вызовите этот метод.'''

'''7 Administrator: Administrator is a special user.
Write a class named Admin and let it inherit from the
User class you wrote for exercise 3. Add an
attribute called privileges to hold a list of strings
(e.g. "can add a message", "can delete a message",
"can block user", etc.). Write a method called
show_privileges() that displays admin rights. Create
an instance of Admin and call this method.'''


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
    def show_privileges(self):
        print(self.first_name.title(), self.last_name.title(), 'can:')
        for i in range(len(self.right)):
            print(str(i)+'.', self.right[i])

andrey=User('andrey', 'antonov', 'flowers', '2mFF04ydZo9MM6v')
michael=Admin('michael', 'kuznetsov', 'car', 's2i1V1F8ue', ["add a message", "delete a message", "block user"])
andrey.describe_user()
andrey.greet_user()
print()
michael.describe_user()
michael.greet_user()
michael.show_privileges()
