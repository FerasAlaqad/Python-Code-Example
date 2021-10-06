# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:56:57 2021

@author: feras
"""

#---------------------------------------------------------------------------------------

#### variabels

# first_name = "feras"
# last_name= "Alaqad"
# full_name=first_name+" " +last_name
# print("hello "+ full_name)
# print(type(full_name))


# age = 21
# age=age+1

# height = 250.55
# print (type(height))
# print("your heigth is: " + str(height)+ "cm")


# human = False
# print(human)
# print(type(human))
# print("are you human: " + str(human))

#---------------------------------------------------------------------------------------

#### multiple assignment


# name, age ,attractive="feras",21,True
# print (name)
# print (age)
# print (attractive)

# a= b = c= d= 30
# print (a)
# age+=1
# print(type(age))
# print(age)
# print("your age is : "+str(age))

# print (b)
# print (c)
# print (d)

#---------------------------------------------------------------------------------------

#### string methods

# name ="feras"
# print(len(name))
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("e"))
# print(name.replace("s", "z"))
# print(name*3)

#---------------------------------------------------------------------------------------

#### type cast

# x=1
# y=2.5
# z= "3"

# str(x)
# print(z*3)
# z=int(z)


# print(x)
# print(int(y))
# print(z*3)

#---------------------------------------------------------------------------------------

#### user input


# name= input("What is your name?")
# age= input("how old are you?")
# heigth =float(input("how tall are you?"))


# age=int(age)+1


# print ("Hello " +name)
# print ("you are "+ str(age)+" years old")
# print("you are "+ str(heigth)+ "cm tall " )

#---------------------------------------------------------------------------------------

#### math functions

# import math

# pi= 3.14
# print(round(pi)) #round down
# print(math.ceil(pi)) #round up
# print(math.floor(pi)) #round down
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(4))

#---------------------------------------------------------------------------------------

#### string slicing

# name = "Feras%Alaqad"
# first_name= name[0:5]
# print(first_name)
# first_name= name[:5]
# print(first_name)
# last_name=name[6:]
# print(last_name)
# reversed_name=name[::-1]
# print(reversed_name)


# website="http://googel.com"
# website2="http://wikipedia.com"

# slice = slice(7,-4) #we should take it as anegative integer because it can be changed
# print(website[slice])
# print(website2[slice])

#---------------------------------------------------------------------------------------

#### if statements

# age=int(input("how old are you?"))


# if age==100:
#     print("you are the eldest")
# elif age >= 18:
#     print("your are an adult")

# elif age<0:
#     print("you haven't born yet")
# else:
#     print("your are a child")

#---------------------------------------------------------------------------------------

#### logical operators

# temp= int(input("what is the temp outside?"))


# if temp>= 0 and temp <= 30:
#     print("the temp is good today")

# elif temp<0 or temp>30:
#     print("the temp is bad today")

#---------------------------------------------------------------------------------------

#### While loops

# name=""
# #while len(name)==0: # the same
# while not name:
#     name=input("Enter your name?")

# print("hello "+ name)
#---------------------------------------------------------------------------------------

#### for loops

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1):
#     print(i)


# for i in range(50,100+1,2):
#     print(i)

# for i in "Feras Alaqad":
#     print(i)

#---------------------------------------------------------------------------------------

#### import time

# for secounds in range(10,0,-1):
#     print(secounds)
#     time.sleep(1)
# print("Happy New Year")
#---------------------------------------------------------------------------------------

#### nested loops

# rows = int(input("How many rows: "))
# columns = int(input("How many colm: "))
# symbol= input("Enter a symbol: ")

# for i in range (rows):
#     for j in range(columns):
#         print(symbol, end="") #dont make new line
#     print()
#---------------------------------------------------------------------------------------

#### break continue pass

# while True:
#     name =input("Enter your name: ")
#     if name!="":
#        break

# phone_number="123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i== 13:
#         pass # dont stay empty
#     else:
#         print(i)
#---------------------------------------------------------------------------------------

#### lists

# names =["ahmet","sami","salih"]

# print(names)
# print(names[0])

# names[0]= "feras"
# print(names[0])

# for i in names:
#     print (i)


# for x in range(len(names)):
#     print (names[x])

# names.append("mahmut")
# names.remove("feras")
# names.pop()
# names.insert(0,"fero")
# names.clear()
# print(names)

#---------------------------------------------------------------------------------------

#### 2D lists

# drinks = ["coffee","soda","tea"]
# dinner =["pizza","hum","hotdog"]
# dessert=["cake","ice cream"]
# food=[drinks,dinner,dessert]

# print(food)
# print(food[0])
# print(food[1])
# print(food[2][1])
#---------------------------------------------------------------------------------------

#### tuples


# student =("feras",21,"male")

# print(student.count("feras"))
# print(student.index(21))

# for x in student:
#     print(x)

# if "feras" in student:
#     print("feras is here")

#---------------------------------------------------------------------------------------

#### sets

# utensils= {"fork","spoon","spoon","spoon","spoon","knife"}
# dishes ={"bowl" ,"plate","cup"}
# dinner_table= utensils.union(dishes)


# print(len(utensils)) # don't see the same values
# utensils.add("napkin")
# utensils.remove("fork")
# #utensils.update(dishes)


# for x in dinner_table:
#     print(x)

# print(dishes.difference(utensils))
# print(dishes.intersection((utensils)))

####---------------------------------------------------------------------------------------

# dictionaries
# A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access avalue quickly
# we can update dictionaries while programe is working

# capitals= {'USA': 'Washington DC',
#            'India': 'New Delhi',
#            'Palestaine': 'jerusalema'
#            }

# print(capitals)
# print(capitals["USA"])
# #print(capitals["Germany"])
# print(capitals.get("Germany")) #more safer
# print(capitals.keys())
# capitals.update({"Germany":"Berlin" })
# capitals.update({"USA":"las vegas" })
# capitals.pop("India")

# for key,value in capitals.items():
#     print(key,value)
#---------------------------------------------------------------------------------------

#### indexing
# gives access to sequence's element(ste, list, tuples)

# name= "feras ALAQAD"

# if(name[0].islower()):
#    name=name.capitalize()

# # print(name)

# first_name=name[0:6].upper()
# print(first_name)

# last_name=name[6:].lower()
# print(last_name)

# last_Chare= name[-1:]
# print(last_Chare)
#---------------------------------------------------------------------------------------


#### functions

# def hello(first_name,last_name,age ):
#     print("hello " + first_name + " "+last_name + ",age: "+str(age))
#     print("Have a nice day")
#     print()


# my_name="feras"

# hello(my_name,"alaqad",21)

#---------------------------------------------------------------------------------------

#### return statement

# def multiply(num1, num2):
#     result= num1*num2
#     return result

# print(multiply(5, 8))
#---------------------------------------------------------------------------------------

#### keyword arguments

# def hello (first, middle,last):
#     print("Hello "+first+" "+middle+" "+last)

# hello(last="ALAQAD",middle="Mohd",first="feras")

# nested function calls

# print (round(abs(float(input("Enter a whole pozitive number:")))))

#---------------------------------------------------------------------------------------

#### variable scope

# name= "feras" # global variable

# def display_name():
#     name="code" # local variable
#     print(name)

# display_name()
# print(name)
#---------------------------------------------------------------------------------------

#### *args

# parameter that will pack all arguments into a tuple
# useful so tha t function can accept a varying amount of arguments

# def add(*stuff):
#     sum=0
#     stuff= list(stuff) #because of stuff unchangebale
#     stuff[0]=0

#     for i in stuff:
#         sum +=i
#     return sum


# print(add(1,2,3,4,5,6,8,9,6))
#---------------------------------------------------------------------------------------

#### **kwargs

# parameter that will pack all arguments inyo a dictionary
# useful so tha t function can accept a varying amount of arguments

#---------------------------------------------------------------------------------------

#### string format

# optional method that gives users more controlwhen
# displaying output

# animal= "cow"
# item= "moon"

# print("The {} jumbed over the {}".format(animal, item))#positional argumants

# test= "The {} jumbed over the {:10} there is a space" #space
# test=test.format(animal, item)
# print(test)

# number = 3.14159
# number1 = 56997

# print("The number pi is {:.3f}".format(number))
# print("The number pi is {:,}".format(number1))
# print("The number pi is {:b}".format(number1))
# print("The number pi is {:o}".format(number1))
# print("The number pi is {:X}".format(number1))
# print("The number pi is {:E}".format(number1))

#---------------------------------------------------------------------------------------

#### random numbers

# import random

# x= random.randint(1, 6)
# y= random.random()

# mylist=["rock","paper", "scissors"]
# cards =[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

# z= random.choice(mylist)
# random.shuffle(cards)

# print(x)
# print(y)
# print(z)
# print(cards)

#---------------------------------------------------------------------------------------

#### exception handling

# events deteceted during execution that interrupt the folw of a program

# try:
#     a= int(input("Enter a number: "))
#     b= int(input("Enter a number: "))
#     result=a/b
#     print(result)

# except ZeroDivisionError:
#     print("Zero something is going wrong")

# except ValueError as e: # we can make it like this
#     print("Value Error something is going wrong")
#     print(e)
# except Exception:
#     print("Exce something is going wrong")

# else:
#     print("else") #if we dont have any exeption it will work
# finally: # it will work whether or not any exception , its important to close the opened files
#     print("finally")

#---------------------------------------------------------------------------------------

#### file detection

# import os


# path= "C:\\Users\\feras\\Desktop\\test.txt"

# if os.path.exists(path):

#     print("that location exists")

#     if os.path.isfile(path):
#         print("That is file")

#     elif os.path.isdir(path):
#         print("That is directiory")


# else:
#     print("that location not exists")

#---------------------------------------------------------------------------------------

#### read a file

# path= "C:\\Users\\feras\\Desktop\\test.txt"

# try:
#     with open(path) as file:
#         print(file.read())

# except FileNotFoundError as  e:
#     print(e)
# except Exception as e:
#     print(e)

#---------------------------------------------------------------------------------------
#### write a file

# text="yooooooooo \nTihs is some text \nHave agood one\n"
# text1="have a nice day "

# with open ("test.txt","w") as  file:
#     for i in range(9):
#        file.write(text)

# with open ("test.txt","a") as  file: # for append
#        file.write(text1)

#---------------------------------------------------------------------------------------

#### Copy a File

# import shutil
# shutil.copyfile("test.txt", "copy.txt")

#---------------------------------------------------------------------------------------
#### moving a file

# import os

# source = "test.txt"
# destination= "C:\\Users\\feras\\Desktop\\test.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file with the same name there")
#     else:
#         os.replace(source, destination)
#         print(source+ " was moved")
# except FileNotFoundError as e:
#        print(e)

#---------------------------------------------------------------------------------------

#### modules

# a filecontaning paython code, May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts.


# import messages as mes

# mes.hello()
# mes.bey()


# help("modules") # all of availabel moudels

#---------------------------------------------------------------------------------------

#### rock, paper, scissors game

# import random

# choices = ["rock", "paper", "scissors"]

# while True:
#  player = None
#  computer = random.choice(choices)
#  while player not in choices:
#      player = input("rock, paper, or scissors ?: ").lower()


#  if player == computer:
#      print()
#      print("player: " + player)
#      print("computer: " + computer)
#      print("Tie!")
#  elif player == "rock":

#     if computer == "paper":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You lose!")

#     if computer == "scissors":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You win!")

#  elif player == "scissors":

#     if computer == "paper":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You win!")

#     if computer == "rock":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You lose!")

#  elif player == "paper":

#     if computer == "scissors":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You lose!")

#     if computer == "rock":
#       print("player: " + player)
#       print("computer: " + computer)
#       print("You win!")

#  play_again= input("Play again? (Y/N)").lower()

#  if play_again != "y":
#      break

# print("Bay")

#---------------------------------------------------------------------------------------
#### Quiz game

# # -------------------------
# def new_game():

#     guesses = []
#     correct_guesses = 0
#     question_num = 1

#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)

#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1

#     display_score(correct_guesses, guesses)

# # -------------------------
# def check_answer(answer, guess):

#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0

# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")

#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()

#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()

#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")

# # -------------------------
# def play_again():

#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()

#     if response == "YES":
#         return True
#     else:
#         return False
# # -------------------------


# questions = {
#  "Who created Python?: ": "A",
#  "What year was Python created?: ": "B",
#  "Python is tributed to which comedy group?: ": "C",
#  "Is the Earth round?: ": "A"
# }

# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

# new_game()

# while play_again():
#     new_game()

# print("Bye!")

# # -------------------------

#---------------------------------------------------------------------------------------
#### Object oriented Programming

# from car import Car

# car_1=Car("chevy","Corvette","2021","blue")
# car_2=Car("Ford","Mustang","2020","red")



# print(car_1.make)
# print(car_1.model)
# print(car_1.color)


# print(car_2.make)
# print(car_2.model)
# print(car_2.color)

# car_1.drive()
# car_1.stop()

#---------------------------------------------------------------------------------------

####class variables


# from car import Car

# car_1=Car("chevy","Corvette","2021","blue")
# car_2=Car("Ford","Mustang","2020","red")

# car_1.wheels=2
# car_2.wheels=4

# Car.wheels=8  # it wil afferct all of classes
#---------------------------------------------------------------------------------------

#### inheritance

# class Animal:

#     alive = True

#     def eat(self):
#         print("This animal is eating")

#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal): # extending

#     def run(self):
#         print("This rabbit is running")

# class Fish(Animal):

#     def swim(self):
#         print("This fish is swimming")

# class Hawk(Animal):

#     def fly(self):
#         print("This hawk is flying")


# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()
#---------------------------------------------------------------------------------------

#### multilevel inheritance

# class Organism:

#     alive = True

# class Animal(Organism):

#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal):

#     def bark(self):
#         print("This dog is barking")


# dog = Dog()
# print(dog.alive)    # inherited from the Organism class
# dog.eat()           # inherited from the Animal class
# dog.bark()          # defined in Dog class
#---------------------------------------------------------------------------------------

#### multiple inheritance
#when a child is derived from more than one parent


# class Prey:

#     def flee(self):
#         print("This animal flees")

# class Predator:

#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass


# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# # rabbit.flee()
# # hawk.hunt()
# fish.flee()
# fish.hunt()
#---------------------------------------------------------------------------------------

#### Override

# class Animal:

#     def eat(self):
#         print("This animal is eating")

# class Rabbit(Animal):

#     def eat(self):
#         print("This rabbit is eating a carrot")


# rabbit = Rabbit()
# rabbit.eat()

#---------------------------------------------------------------------------------------

#### Method chaining 
# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

# class Car:

#     def turn_on(self):
#         print("You start the engine")
#         return self

#     def drive(self):
#         print("You drive the car")
#         return self

#     def brake(self):
#         print("You step on the brakes")
#         return self

#     def turn_off(self):
#         print("You turn off the engine")
#         return self


# car = Car()

# # car.turn_on().drive()
# # car.brake().turn_off()
# #car.turn_on().drive().brake().turn_off()

# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

#---------------------------------------------------------------------------------------

####Super Function 
# in java super already have writtin in all of method. But in python not.

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):

#     def __init__(self, length, width):
#         super().__init__(length,width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):

#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height

#     def volume(self):
#         return self.length*self.width*self.height


# square = Square(3, 3)
# cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())

#---------------------------------------------------------------------------------------

#### Abstract 


#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class
# you can make a non abstract method in abstract class 

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")

#     def stop(self):
#         print("This car is stopped")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")

#     def stop(self):
#         print("This motorcycle is stopped")


# #vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()

# #vehicle.go()
# car.go()
# motorcycle.go()

# #vehicle.stop()
# car.stop()
# motorcycle.stop()
#---------------------------------------------------------------------------------------

#### Pass Object as an Argumant
 
# class Car:

#     color = None

# class Motorcycle:

#     color = None

# def change_color(vehicle,color):

#     vehicle.color = color


# car_1 = Car()
# car_2 = Car()
# car_3 = Car()

# bike_1 = Motorcycle()

# change_color(car_1,"red")
# change_color(car_2,"white")
# change_color(car_3,"blue")
# change_color(bike_1,"black")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

#-------------------------------------------------------------------------------------------

####Python Duck typing

# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

# class Duck:

#     def walk(self):
#         print("This duck is walking")

#     def talk(self):
#         print("This duck is qwuacking")

# class Chicken:

#     def walk(self):
#         print("This chicken is walking")

#     def talk(self):
#         print("This chicken is clucking")

# class Person():

#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")


# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)
# person.catch(duck)

#---------------------------------------------------------------------------------------
#### walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression



# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)

#---------------------------------------------------------------------------------------
#### assign a function to a variable


# def hello():
#     print("Hello")


# hi = hello
# hi()

# # say = print
# # say("Whoa! I can't believe this works! :O")


#---------------------------------------------------------------------------------------
####Higher Order Function 
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)


# #return a function

# def divisor(x):
#     def divided(y):
#         return y/x
#     return divided

# exp= divisor(3)
# print(exp(9)) ## we gave exp the same adress of divided 


# #accepts a function as an argument

# def loud(text):
#     return text.upper()

# def quiet(text):
#     return text.lower()

# def say(function,word):
#     print(function(word))
    
# say(loud,"Feras")    
# say(quiet,"Feras")    

#---------------------------------------------------------------------------------------
####lambda function

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# double= lambda x: x*2
# Multi= lambda x,y: x*y
# full_name= lambda first_name, last_name : first_name+" "+last_name
# age_check= lambda age: True if age>18 else False

# print(double(5))
# print(Multi(5,20))
# print(full_name("Feras","ALAQAD"))
# print(age_check(12))
# print(age_check(19))



#---------------------------------------------------------------------------------------
#### sort
# sort() method   = used with lists
# sort() function = used with iterables


#list
# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr.Krabs","C", 78))

# grade = lambda grades:grades[1]
# # students.sort(key=age)                     # sorts current list
# sorted_students = sorted(students,key=grade) # sorts and creates a new list

# age = lambda ages:ages[2]
# # students.sort(key=age)                     # sorts current list
# sorted_students = sorted(students,key=age) # sorts and creates a new list

# for i in sorted_students:
#     print(i)



#iterabels

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr.Krabs","C", 78)]

# grade = lambda grades:grades[1]
# students.sort(key=grade,reverse=False)

# for i in students:
#     print(i)



#---------------------------------------------------------------------------------------
#### maps 
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)


# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]

# to_euros= lambda data : (data[0],data[1]*0.82)
# store_euros= list(map(to_euros,store))
# for i in store_euros:
#     print(i)
#---------------------------------------------------------------------------------------
####filter


# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)


# friends = [("Ahmet",15),
#           ("Mohammet",18),
#           ("ismet",19),
#           ("feras",25)]

# age = lambda ages: ages[1]>=18
# accepted= list(filter(age, friends))

# for i in accepted:
#     print(i)



#---------------------------------------------------------------------------------------
#### Reduce Function 


# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)


# import functools

# letters=["H","E","L","L","O"]
# word= functools.reduce(lambda x,y : x+y,letters)
# print(word)

# Numbers=(5,4,3,2,1)
# Factorial= functools.reduce(lambda x,y : x*y,Numbers)
# print(Factorial)




#---------------------------------------------------------------------------------------
####list comprehension 


# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]


# squares = []   
#              # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append(i * i)    # define what each loop iteration should do
# print(squares)

# # create a list AND defines what each loop iteration should do
# squares = [i * i for i in range(1,11)]
# print(squares)



# students= [100,90,80,70,60,50,40,30,20,10]

# passed_students1= list(filter(lambda x : x>=60, students))
# print(passed_students1)

# passed_students2= [i for i in students if i>=60]
# print(passed_students2)

# passed_students3= [i if i>=60 else "Failed"  for i in students ]
# print(passed_students3)

#---------------------------------------------------------------------------------------
#### dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)


#---------------------------------------------------------------------------------------
####Zip Function 

# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_dates = ["1/1/2021","1/2/2021","1/3/2021"]


# users = list(zip(usernames,passwords))

# for i in users:
#     print(i)

# users = dict(zip(usernames,passwords))

# for key,value in users.items():
#     print(key+" : "+value)

# users = zip(usernames,passwords,login_dates)

# for i in users:
#     print(i)



#---------------------------------------------------------------------------------------

# if __name__ == '__main__'

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run




#---------------------------------------------------------------------------------------
####Time

# import time

# print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
# #                                        epoch = when your computer thinks time began (reference point)
# print(time.time())      # return current seconds since epoch
# print(time.ctime(time.time())) # will get current time



# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)


# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)


# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)


# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)



#---------------------------------------------------------------------------------------

#Yani biz multithread bir programlamada aynı process içindeki thread sayısını 
#artıracağız ama multiprocessing bir programlamada kaynak sayısını yani process
#sayısını artıracağız


#---------------------------------------------------------------------------------------

#### Python threading tutorial


# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading



# import threading
# import time


# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")


# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")


# def study():
#     time.sleep(5)
#     print("You finish studying")


# x = threading.Thread(target=eat_breakfast, args=())
# x.start()

# y = threading.Thread(target=drink_coffee, args=())
# y.start()

# z = threading.Thread(target=study, args=())
# z.start()

# # x.join()
# # y.join()
# # z.join()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())



#---------------------------------------------------------------------------------------

#### Python daemon threads

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

# import threading
# import time


# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", count, "seconds")


# x = threading.Thread(target=timer, daemon=True)
# x.start()

# # x.setDaemon(True)
# # print(x.isDaemon())

# answer = input("Do you wish to exit?")




#---------------------------------------------------------------------------------------

#### multiprocessing 

 # Python multiprocessing
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

# from multiprocessing import Process, cpu_count
# import time


# def counter(num):
#     count = 0
#     while count < num:
#         count += 1


# def main():

    # print("cpu count:", cpu_count())

    # a = Process(target=counter, args=(500000000,))
    # b = Process(target=counter, args=(500000000,))

    # a.start()
    # b.start()

    # print("processing...")

    # a.join()
    # b.join()

    # print("Done!")
    # print("finished in:", time.perf_counter(), "seconds")


# if __name__ == '__main__':
#     main()


#---------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------





# print(foods)

