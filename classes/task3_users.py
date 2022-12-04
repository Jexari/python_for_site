#3 Пользователь: создайте класс с именем User, который
#содержит атрибуты first_name и last_name, а также
#несколько других атрибутов, которые обычно хранятся в
#профиле пользователя. Определите метод с именем
#describe_user () в классе User, который печатает
#сводную информацию о пользователе; определите метод с
#именем greet_user (), который отправляет
#персонализированное приветствие пользователю.
#Создайте несколько экземпляров, представляющих разных
#пользователей, и вызовите два вышеуказанных метода
#для каждого экземпляра.

#3 User: Create a class named User that contains the
#first_name and last_name attributes, as well as a few
#other attributes that are typically stored in a user
#profile. Define a method called describe_user() in
#the User class that prints summary information about
#the user; define a method named greet_user() that
#sends a personalized greeting to the user.
#Create multiple instances representing different
#users and call the above two methods on each instance.

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
andrey=User('andrey', 'antonov', 'flowers', '2mFF04ydZo9MM6v')
michael=User('michael', 'kuznetsov', 'car', 's2i1V1F8ue')
andrey.describe_user()
andrey.greet_user()
print()
michael.describe_user()
michael.greet_user()
