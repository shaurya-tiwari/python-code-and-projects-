import maths
print("_________________________________________________________________________________________________________________________________________________________")
print("-----------------------------------------------------------------!! OM GANESHAYE NAMAH !! ------------------------------PYTHON ")
print("_____________________________________________________________________________________________________________________________________________________________________________")
# object orieented programing


# classes
# class Factory:
#     a = 12  # attribute

#     def hello(self):  # this is method (the fuunction inside the class)
#         print("heloo from method of class")


# print(Factory().a)  # access attribute
# Factory().hello()  # call method


# # Objects
# obj = Factory()  # first it was variabel but after the assign it class it becames object
# print(obj.a)  # now you can access mehod directly from object.
# obj.hello()  # calling method .


# constructor
# class Factory:
#     # self = location of variable like ex: 100 is location then 100.meterial,100.zips
#     def __init__(self, materials, zips, pockets):
#         # assign vlues in arguments
#         self.material = materials
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"your obects are :  {self.material},{self.zips},{self.pockets}")


# reebok = Factory("lethers", 3, 5)

# coach = Factory("pure lether", 2, 1)

# coach.show() #print all objects of coach


# attributes and method
#  attribbutes: define inside the class
# class Animal:
#     name = "lion"  # class atrribute

#     def __init__(self, age):
#         self.age = age  # instance attributes : target the instance , meas object location

#     def show(self):  # instance method
#         print(f"print from show functtion , and target he age : {self.age}")

#     @classmethod  # decorator
#     def hello(cls):  # here we cant use self becoause self use to target the obect location and iinstance
#         # cls is target the classs location
#         print("heloo for the class decorator , means its target the animal class ")

#     @staticmethod
#     def static():  # we dont need to use the parameter here becousee ts static
#         print("heloo form the static method ")


# obj = Animal(20)
# obj.show()  # it akwsy work with arguments
# obj.hello()  # it will not taret teh animal age
# obj.static()


# pillars of oops
# 1. Inheritance : work with in clases
# class Factory:  # parent class / superclass
#     a = "i am attrbute inside the class Factory "  # class attribute

#     def hello(self):  # method
#         print("hello froo method inside the class")


# class FactoryPune(Factory):  # child class / subclasss
#     # inherite the property of base class "Factory"
#     pass


# obj = FactoryPune()  # inherite the properties of super class
# print(obj.a)


# constructor in inheritence
# class Animal():
#     def __init__(self, name):  # constructorr  function
#         self.name = name

#     def show(self):
#         print(f"helo from animal class function and name is : {self.name}")


# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name) # here super class target teh parent classs , mens the name will automatically initialize
#         # initialize age
#         self.age=age


# animal1 = Animal("lionn")
# animal1.show()
# # inherited class
# person1 = Human("agent kabir")  # name set to animal cllass name attribute
# person1.show()

# types - single  level multiple inheritence ,
# multiple inheritence ______
# class Animal():
#     def __init__(self, name):
#         pass


# class Human():
#     def __init__(self, name, age):
#         pass


# class Robot(Animal, Human):
#     name3 = 'chitti'


# # ttyhhe targeted parameter will be thrr order of parameter set in the Robot(animal,human) robbot(human,  animmal)
# obj = Robot()


# multilevel inheritence
# class factory():
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips


# class bhopalfactory(factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color


# class punefactory(bhopalfactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pocket = pockets


# obj = punefactory("nylon", 10, "black", 20)

# hirarchy inheritence - two child subclass inherit same super class


# ___________polymorphism ______________________
# same name having many diffrent forms
# methodoverridingand method method overloading


# Duck typing


# Encapsulationn ______________________________
# access modifier
# protected : (_) annotation ... useless no use

# private method : use (__) two undderscore
# class Factory():
#     __a = 'pune'  # private , double underscore

#     def __show(self):  # double undrscore
#         print('hello i am pune factory')


# class bhopal(Factory):
#     def show2(self):
#         # now it will cant acces a becouse its anoteted from 2 parameters
#         print(super().__a)


# obj = bhopal()
# obj.show2()  # no accesbible


# dunder method
# specil method sstart end end with double underscore (__init__)
# class Animal():
#     def __init__(self, nme, age):
#         self.nme = nme
#         self.age = age

#     def __str__(self):    # its target ttself directly in object | no need to call function , we just have to print
#         return f"heloo dunder __str__{self.nme}"

#     def __add__(self, other):
#         return f"sum age {self.age + other.age}"


# obj = Animal("kabir", 10)
# obj2 = Animal("shaurya", 10)
# print(obj+obj2)  # print things directly


# args and kwargs |* , **

# args
# or multiple  paramters and arguments capturing
# def addition(*args):  # after adding * it will became tuple
#     sum = 0
#     for i in args:
#         sum = sum+i

#     print(sum)


# addition(12, 23, 4, 5,)


# kwargs : ** keywordarguments - capture key and value
# def information(**kwargs):
#     print("print your infrmation \n\n")
#     for i in kwargs:
#         print(f"{i} ; {kwargs[i]}")


# information(name="kabir", age=23, deignationn="AI/ML engineer")
# output_______________________
# name ; kabir
# age ; 23
# deignationn ; AI/ML engineer


# decorators
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("the aditiion to your number are ")
#         func(*args, **kwargs)
#         print("thankuou i hope u liked it ")
#     return wrapper


# @decorator
# def addition(a, b):
#     print(f"yout total is {a+b}")


# addition(10, 20)


# comprehensives
# ternary opertors
# a=13
# print("evn") if a%2==0 else print("odd")


# list comprehensonn
# this code is for print even numbers in list from 1 to 21
# l = [i for i in range(1, 21) if i % 2 == 0]
# print(l)

# dicctionary comprehnsive
# l = {i: i**2 for i in range(1, 10)}  # print square of numbers from 1 to 10
# print(l)


# lambda funcion : we dont need to ue fucntion as normal
# add = lambda a,b : a+b
# print(add(10,10))

# def add(a): lambda x: "even" if a % 2 == 0 else "odd"

# print(add(3))


# map filter and zip
# a = [1, 2, 3, 4, 5]
# result = map(lambda x: x*2, a)

# print(list(result))
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# itr = [1, 2, 3, 4, 4, 5, 66,]
# # line says that in which function , ittration will done  (functionnae , list )
# result = filter(even, itr)

# print(list(result)) # output = [2, 4, 4, 66] only even is filter from the list ( if true its even )


# modules and packages
# import from otherr file
# print(maths.add(2, 4))
# print(maths.mul(2, 2))
