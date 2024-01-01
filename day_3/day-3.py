age = 22
height = 1.80
complex_num = 1+1j

triangle_base = float(input('Enter base : '))
triangle_height = float(input('Enter height : '))

print('The area of the triangle is : ', 0.5 * triangle_base * triangle_height)

a_side = float(input('Enter side a : '))
b_side = float(input('Enter side b : '))
c_side = float(input('Enter side c : '))

print('The perimeter of the triangle is ', (a_side+b_side+c_side))

length = float(input('Enter length : '))
width = float(input('Enter width : '))

print('Area of the rectangle is', (length*width))
print('Perimeter of the rectangle is', (2*length+2*width))

radius = float(input('Enter radius : '))

print('Area of the circle is ', 3.14*radius*radius)
print('Circumference of the circle is ', 2 * 3.14 * radius)

python = 'python'
dragon = 'dragon'

print(len(python) != len(dragon))

print('on' in python and 'on' in dragon)

print('jargon' in 'I hope this course is not full of jargon')

print(str(float(len(python))))

num = int(input('Enter a number : '))

print(0 == (num % 2))

print(7//3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours = float(input('Enter hours : '))
rate = float(input('Enter rate : '))

print('Your weekly earning is ', hours * rate)

year = int(input('Enter years : '))
print('You have live for' ,year*31536000, 'seconds')

print(
    '\n',
    1,1,1,1,1,'\n',
    2,1,2,4,8,'\n',
    3,1,3,9,27,'\n',
    4,1,4,16,64,'\n',
    5,1,5,25,125
)