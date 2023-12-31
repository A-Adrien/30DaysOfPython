# Day 2: 30 Days of python programming

first_name = input('firstname : ')
last_name = input('lastname : ')
full_name = 'Adrien A'
country = input('country : ')
city = 'Paris'
age = int(input('age : '))
year = 2023
is_married = False
is_true = True
is_light_on = False
a, b, c = 'a', 21, ['bla', 23]

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))


print('The lenght of your firstname is ', len(first_name))
print('The lenght of your lastname is ', len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

import math

radius = float(input('Enter a radius : '))
area_of_circle = math.pi * (radius**2)
circum_of_circle = (2*math.pi) * radius
print('Area : ', area_of_circle)

help('keywords')