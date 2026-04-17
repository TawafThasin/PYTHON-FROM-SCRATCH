#input function allows us to get a specific message to display and returns the value typed in by the user 
#name refers to the one which will be coming as the output we can use any word there but needs to match with the print one


#collect name from the user
name = input("What is your name? ")
#display the name
print(name)


#update the value
name = 'Tawaf Thasin'
print(name)


#triple quote helps me to put a long string
name = '''Hello, This is Tawaf. Nice to meet you! '''
print(name)


#return character of the values 
name = 'I am loving python'
print(name[3])
print(name[4:15])


#defining strings 
firstname = 'Tawaf'
secondname = 'Thasin'
output = f'{firstname} [{secondname}] is a coder'


#count number of strings
name = 'Tawaf'
print(len(name))



#can combine variables and strings with the + sign
firstname = input('What is your first name? ')
secondname = input('What is your second name? ')
print(firstname + secondname)


#create a friendly output
name = input('What is your name? ')
print('Hello, ' + name)


#.upper makes it all caps .lower makes it all low
name = input('What is your last name? ')
country = input('What country do you live in? ')
country = country.upper()
print('Hello, ' +  name + '. You live in '  + country)


#some of the new different functions are shown below-
message = 'Hello world'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
print(message.replace('Hello', 'Hi'))
print('World' in message)


#calculate the area of a triangle (just an example, can do with any other shapes
name = input('What will be the area of the desired triangle with the value of the width 20 and height 10?')
area = 0
width = input('What is the width? ')
print(width)
height = input('What is the height? ')
print(height)
area = (width * height * 1/2)
 

#printing formated float value with 2 decimal places
print("The area of the triangle would be %2f" % area)
#printing the formated decimal number
print('My favorite number is %06d !' % 42)


#printing the format with the .format syntax
print('The area of the triangle would be {0:f} '.format(area))
print('My favorite number is {0:d} '.format(42))


#printing the format with multiple numbers using the .format syntax (just an example)
#i can use a \ sign to continue the command to the second line and forth
print('Here are three numbers! The first is {0:d} + \
       The second is {1:4d} The third is {2:d}'.format(7,8,9))





