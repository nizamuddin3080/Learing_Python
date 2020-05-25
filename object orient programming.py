# class person:
#     def __init__(self, name, age):
#         self.student_name = name
#         self.student_age = age
#
#     def get_name(self):
#         return self.student_name
#
#     def set_name(self, new_name):
#         if self.__has_any_number(new_name)
#         print("sorry number can't be name")
#         self.name = new_name
#
#     def __has_any_number(self, string):
#         if "0" in string


#
#
#
#
#
# class student(person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.student_roll = roll
#
#     def get_summery(self):
#         return f"Name: {self.student_name}, Age: {self.student_age}, Roll: {self.student_roll}"
#
# student_information = student("shahid", 12, 23)
#
# print("welcome", student_information.student_name)
#
#
#
#
#


# class person:
#     def __init__(self, name, age):
#         self.student_name = name
#         self.student_age = age
#
#
# class student(person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.student_roll = roll
#
#     def get_summery(self):
#         return f"Name: {self.student_name}, Age: {self.student_age}, Roll: {self.student_roll}"
#
#
# student_information = student("Nizam", 21, 2)
#
# print("This is", student_information.student_name, "which age is", student_information.student_age, "and roll is",
#       student_information.student_roll)
#
#
#

#
# class person:
#     def __init__(self, name, age):
#         self.student_name = name
#         self.student_age = age
#
#
# class student(person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.student_roll = roll
#
#     def welcome(self):
#         print("This is", self.student_name, "which Age is", self.student_age, "and his roll in the class", self.student_roll)
#
# x = student("Nizam", 21, 23)
# x.welcome()
#
#


# class Person:
#     def __init__(self, name, age):
#         self.student_name = name
#         self.student_age = age
#
#
# class Student(Person):
#     def __init__(self, name, age, roll):
#         super().__init__(name, age)
#         self.student_Roll = roll
#
#     def get_summery(self):
#         return f"Name: {self.student_name}, Age: {self.student_age}, Roll: {self.student_Roll}"
#
#
# x = Student("Nizam", 520, 38)
# print(x.get_summery())
#
# print("This is", x.student_name, "which Age is", x.student_age, "and his roll in the class", x.student_Roll)


# ____________________________________________________________________________________________________________
#
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#
#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
#
# x = Student("Mike", "Olsen", 2019)
# x.welcome()
