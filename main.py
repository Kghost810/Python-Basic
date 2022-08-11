"""import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%&*?"

Use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 8
password = "".join(random.sample(Use_for, length_for_pass))
print(password)

name_of_students = ["Kwabena", "Ama", "Kofi", "Kojo"]
for student in name_of_students:
    print(f"{student} is a brilliant student.")
    age = 22
if age >= 18:
    print("You are eligible to vote during this general elections.")
    print("Have you registered to vote already?")
else:
    print("You are not old enough to vote.")

age = 18
if age < 6:
    print("Cost of registration is $0")
elif age <= 17:
    print("Cost of registration is $25")
else:
    print("Cost of registration is $45")
age = 20
if age < 6:
    cost = 0
elif age <= 17:
    cost = 25
elif age < 65:
    cost = 40
else:
    cost = 50/100 * 40
print(f"Yours cost of admission is ${cost}.")
alien_color = 'gold'
if alien_color == 'green':
    print("You have earned 5 points.")
elif alien_color == 'yellow':
    print("You have earned 10 points.")
elif alien_color == 'red':
    print("You have earned 15 points.")
else:
    print("Try again!")
age = 65
if age <2:
    stage_of_life = 'baby'
elif age <= 3:
    stage_of_life = 'toddler'
elif age <= 12:
    stage_of_life = 'kid'
elif age <= 19:
    stage_of_life = 'teenager'
elif age <= 64:
    stage_of_life = 'adult'
else:
    stage_of_life = 'elder'
print(f"The person is a/an {stage_of_life}")
favorite_fruits = ['mango', 'berry', 'banana']
if 'orange' in favorite_fruits:
    print("You like oranges")
if 'berry' in favorite_fruits:
    print("You like berry")
if 'mango' in favorite_fruits:
    print("You like mango")
if 'tomato' in favorite_fruits:
    print("You like tomato")
if 'banana' in favorite_fruits:
    print("You like banana")
usernames = ['ben', 'joel', 'daniel','admin', 'george']
for name in usernames:
    print(f"Hello {name.title()}, thank you for logging in again.")
    if 'admin' in usernames:
        print(f"Hello {name.title()}, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")

game = {'color': 'red', 'point': 5}
new_point = game['point']
print(f"You have earn {new_point} points.")

alien = {'color': 'green', 'point': 5 }
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

friends = ['kwame', 'ama', 'kwabena']
print(friends)
friends.append('kwaku')
print(friends)

kapo_age = {}
kapo_age['aaron'] = 22
kapo_age['agyeman']= 24
kapo_age['guy']= 25
print(kapo_age)

alien_0 = {'color_1': 'red'}
message_1 = (f"The alien is {alien_0['color_1']}!")
print(message_1)
alien_0['color_1'] = 'brown'
message_2 =(f"The alien is now {alien_0['color_1']}!")
print(message_2)
alien_0 = {'x_position': 50, 'y_position': 25, 'speed': 'fast'}
message = (f"The alien's original position is {alien_0['x_position']}!")
print(message)
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 10
elif alien_0['speed'] == 'medium':
    x_increment = 20
else:
#Alien must be fast!
    x_increment = 40
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
message = (f"The alien's new position is {alien_0['x_position']}.")
print(message)

age_of_friends = {'Kwabena':24, 'Angela':22, 'Albert':27, 'Emmanuel':33}
age_of_friends['Ben'] = 14
age_of_friends['Salifu'] = 70
print(age_of_friends)
message = (f"It's funny how Kwabena behaves like a child. He is {age_of_friends['Kwabena']} years old.")
print(message)
del age_of_friends['Salifu']
print(age_of_friends)""
"""
"""user_0 = {
    'username': 'kwebena810',
    'firstname': 'kwabena',
    'lastname': 'agyepong'
}
for key, value in user_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.title()}")"""
"""favorite_languages = {
    'Kwabena': 'python',
    'Ben' : 'c++',
    'Agyeman' : 'Java',
    'Kwaku' : 'Java script'
}
for name, language in favorite_languages.items():
    message = (f"{name.title()}'s favorite programming language is {language.title()}!\n")
    print(message)"""
"""favorite_languages = {
    'Kwabena': 'python',
    'Ben' : 'c++',
    'Agyeman' : 'Java',
    'Kwaku' : 'Java script'
}
friends = ['kwabena', 'ben']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")"""
"""date_of_birth = input("Please enter your birth year: ")
age = 2022 - int(date_of_birth)
message = (f"You are currently {age} years old!")
print(message)"""
"""name_of_friends = ['kwabena','aaron','ben','joel']
for friend in name_of_friends:
    message = (f"{friend.title()}'s best language is Python!")
    print(message)"""
"""fruits = {
    'apples': 27,
    'berries': 34,
    'mangoes':37,
    'banana': 25
}
for fruit, fruit_quantity in fruits.items():
    print(f"The number of {fruit.title()} in the basket is {fruit_quantity}!")"""
"""best_languages = {
    'kwabena': 'python',
    'ben': 'c++',
    'agyeman': 'Java',
    'kwaku': 'Java',
    'joel': 'react js'
}
print("The following are the list of my best languages!")
for language in set(best_languages.values()):
    print(language.title())"""
"""programming_languages = {'java','python','ruby','java','react'}
for language in programming_languages:
    print(language.title() + " is one of the world's most powerful programming languages.")"""
"""major_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'niger': 'guinea',
    'mississippi': 'minnesota',
    'zaire': 'congo'
}
for river, country in major_rivers.items():
    print(f"The river {river.title()} run through {country.title()}.")

major_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'niger': 'guinea',
    'mississippi': 'minnesota',
    'zaire': 'congo'
}
for river in sorted(major_rivers.values()):
    print(river.title())"""
"""alien_0 = {'color': 'green', 'points': 6}
alien_1 = {'color': 'yellow', 'points': 20}
alien_2 = {'color': 'red', 'points': 38}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)"""
"""Make an empty list for storing aliens.
aliens = []
    #Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    # Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
    #Show how alien have been created!
print(f"Total number of aliens: {len(aliens)}")

        #Shore information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}
        #Summarize the order.
print(f"You have ordered a {pizza['crust']} crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)
favorite_languages = {
    'kwabena':['python', 'c++'],
    'agyeman': 'c',
    'albert': ['c', 'java'],
    'george': ['java script', 'c'],
    'joel': ['python', 'java']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()} loves programming in the following languages: ")
    for language in languages:
        print(f"\t{language.title()}")"""
"""age_of_student = input("Please enter you age: ")
age_of_student = float(age_of_student)
if age_of_student < 6:
    price = 0
elif age_of_student <= 17:
    price = 25
elif age_of_student <= 18:
    price = 30
elif age_of_student < 25:
    price = 40
elif age_of_student >= 50:
    price = (40 / 2)
message = (f"You are supposed to pay an amount of ${price} as entry fee.")
print(message)

height = input("Please enter your height in metres(m): ")
height = float(height)
weight = input("Please enter your current weight in kilograms(kg): ")
weight = float(weight)
bmi = weight / (height * height)
if bmi <= 18.5:
    health_status = (f"underweight")
elif bmi <= 24.9:
    health_status = (f"normal")
elif bmi <= 25:
    health_status = (f"overweigth")
else:
    health_status = (f"oberse")
message = (f"You body mass index shows that you are {health_status}!")
print(f"{message}\n"
      f"Visit you doctor more health tips")
      list_of_cars = ['maseratti', 'camry', 'corolla', 'benz','chevollet' ]
car = input("Please enter the car brand you wanna buy: ")
if list_of_cars == car:
    print(f"Let me see if I can get you the right color of the {car.title()}."
          f"I will be back in a few minutes!")
else:
    print(f"We do not have the brand of car you want" 
          f"I am really sorry for the inconvenient")
"""
"""i = 1
while True:
    if i % 3 == 0:
        break
    print(i)

    i += 9?"""
"""def brave(username):
    print(f"Hello, {username.title() }")
brave("kwabena")

def pet_describtion(pet_name, animal_type):
    print(f"I have a {animal_type} as a pet.\n"
          f"The name of my {animal_type} is {pet_name}!")
pet_describtion(animal_type='dog', pet_name='Scooby')"""
"""def brave(username, user_age = 14):
    print(f"{username.title()} is a {user_age} year old boy!")
brave(username="kwabena")

def make_shirt(shirt_size, front_message = "BE LEGENDARY"):
    print(f"When I got to the market I saw a nice shirt with a "
          f"message {front_message} in front!")
    print(f"Unfortunately it is size {shirt_size} "
          f"which is too small for you!")
make_shirt(14)

def describe_city(city_name,country_name):
    print(f"{city_name} is in {country_name}")
describe_city(city_name='Accra',country_name= "Ghana")"""
"""def formal_name(first_name, last_name, other_name= ""):
    if other_name:
        full_name = f"{first_name} {other_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = formal_name("george","agyapong", "kwabena")
print(name)"""
"""def brave(first_name, last_name):
    full_name = {'first': 'first_name', 'last': 'last_name'}
    return full_name
name = brave('kwabena', 'agyapong')
print(name)"""
"""def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print(f"Please enter you full name.")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    formal_name = formatted_name(first_name, last_name)
    print(f"Hello {formal_name}")"""
"""def greet_users(names):
    for name in names:
        message = f"Hello {name.title()}"
        print(message)

username = ["kwabena","ben",'ama']
greet_users(username)"""
"""unprinted_design = ['Phone case','Robot Pendant', 'Dodecahedron']
completed_designs = []
while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing models: {current_design}")
    completed_designs.append(current_design)

print("\nThe following models have been printed:")
for completed_design in completed_designs:
    print(completed_design)
"""
"""class Dog:
#A simple attempt to model a dog
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    def sit(self):
        
        print(f"{self.name} is now sitting!")
    def roll_over(self):

        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
young_dog = Dog('Billy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dog's name is {young_dog.name}.")
print(f"My dog is {young_dog.age} years old.")
young_dog.sit()
young_dog.roll_over()"""

"""class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, time):
        self.name = restaurant_name
        self.type = cuisine_type
        self.time = time
    def describe_restaurant(self):
        print(f"I love going to {self.name}.")
        print(f"I prefer their {self.type} when i visit.")
    def open_restaurant(self):
        print(f"\nThe restaurant opens at {self.time}.")


my_restaurant = Restaurant("Movenpick", "French Cuisine", "7am")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()"""
"""class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

my_car = Car(2022, 'c300', 'benz')
print(my_car.description_name())

my_car.update_odometer(23)
my_car.read_odometer()

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.description_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()"""
"""class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@yahoo.com'
    def describe_employee(self):
        print(f"{self.email}")

emp_1 = Employee('Kwabena', 'Agyapong', 5000)
emp_2 = Employee('Jay', 'Tee', 2883)
emp_1.describe_employee()
emp_2.describe_employee()"""
"""class Car:
  def __init__(self, manufacturer, model, year):
    self.manufacturer = manufacturer
    self.model = model
    self.year = year
    self.odometer_reader = 0
  
  def descriptive_name(self):
    long_name = f"{self.year} {self.manufacturer} {self.model}"
    return long_name.title()
  
  def odometer_reader(self):
    print(f"Give out the exact {odometer_reader} of the car.")
  
  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles
  
class ElectricCar(Car):
  def __init__(self, manufacturer, model, year):
    super().__init__(manufacturer, model, year)
    self.battery_size = 75
    
  def car_batter_size(self):
    print(f"The car has a {self.battery_size}-kwh battery.")
  
my_car = ElectricCar('tesla', 'model-s', 2022)
print(my_car.descriptive_name())
my_car.car_batter_size()

"""
"""with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())"""

"""filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't devide 5 by zero!")"""

"""print("Enter two numbers and i will divide them for you.")
print("\tEnter 'q' to quit!!!\n")
while True:
    first_number = float(input("First Number: "))
    if first_number == 'q':
        break
    second_number = float(input("Second Number: "))
    if second_number == 'q':
        break
    try:
        division = first_number / second_number
        print(division)
    except ZeroDivisionError:
        print("You can't devide by zero!")
    else:
        print(division)"""

"""filename = 'pi_digits.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file : Filename doesn't exist!")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words in total.")"""
"""def count_word(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("The file : Filename doesn't exist!")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words in total.")
count_word(filename= 'pi_digits.txt')"""
"""import json
numbers = [2, 3, 4, 8, 5]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)"""

"""import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print(f"We'll remember you when you come back, {username}!")
"""
"""import json

username = input("What is your name: ")
filename = 'username.json'
with open(filename, 'w') as file:
    json.dump(username, file)
    print(f"Thanks for contacting us, {username}")

import json
filename = 'username.json'
with open(filename) as file:
    username = json.load(file)
    print(f"Welcome back, {username}")"""

