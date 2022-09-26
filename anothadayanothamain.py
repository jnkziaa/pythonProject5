import re
import time

# password validation
print("A website requires the users to input username and password to register. Write a program to check the validity "
      "of password input by users.\n")


def val_pass():
    input_password = input("Please Enter a password: ")
    pass_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,12}$"
    if re.match(pass_pattern, input_password):
        print("Valid Password! Good Job!")
    else:
        print("Invalid Password! Please Try Again!")
        val_pass()


val_pass()

time.sleep(1)
# sort program
print("----------------------------------------------------------------------------------------------")

print("Question:You are required to write a program to sort the (name, age, height) tuples by ascending order where "
      "name is string, age and height are numbers. The tuples are input by console. The sort criteria is:")
print("1: Sort based on name")
print("2: Then sort based on age")
print("3: Then sort by score.")

list_size = int(input("Please enter how long the list is: "))


def set_up(input_par):
    tuple_size = []
    list_of_tuple = []
    for i in range(input_par):
        values = input("Please input Name, age, and score separated by commas: ")
        tuple_size = values.split(",")
        list_of_tuple.append(tuple_size)

    return list_of_tuple


def sort_this(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0


def sort_key(list_ele):
    return list_ele[0]


print(sorted(set_up(list_size), key=sort_key()))

time.sleep(2)
# use yield divisible by 7
print("-----------------------------------------------------------------------------------------------")

print("Question:Define a class with a generator which can iterate the numbers, which are divisible by 7, between a "
      "given range 0 and n.")

list_range = int(input("Please enter a number for range: "))


def create_generator(input_par):
    mylist = range(input_par)
    for i in mylist:
        if i % 7 == 0:
            yield i


generator = create_generator(list_range)

print("Numbers from 0 to", list_range, "and divisible by 7 are: ")
for x in generator:
    print(x)

time.sleep(2)
# robot moves
print("--------------------------------------------------------------------------------------------")
print("A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, "
      "LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:")


def __prompt():
    list_size = int(input("Please enter how many directions you want to move to: "))
    __number = int(list_size)
    if __number > 4 or __number < 1:
        print("\nPlease only select between 1-4")
        return __prompt()
    else:
        return __number


def set_up(input_par):
    tuple_size = []
    list_of_tuple = []
    for i in range(input_par):
        values = input("Please input Directions and Steps, separated by space: ")
        tuple_size = values.split(" ")
        list_of_tuple.append(tuple_size)

    return list_of_tuple


def calculate_movements(input_par):
    up = 0
    down = 0
    left = 0
    right = 0

    for i in range(len(input_par)):
        direct = input_par[i][0]
        movements = int(input_par[i][1])
        if direct.lower() == "up":
            up += movements
        elif direct.lower() == "down":
            down += movements
        elif direct.lower() == "left":
            left += movements
        else:
            right += movements

    x = abs(up - down)
    y = abs(left - right)

    return abs(x + y)


print("total steps taken is ", calculate_movements(set_up(__prompt())))

time.sleep(1)
# frequency
print("--------------------------------------------------------------------------------------------")
print("Write a program to compute the frequency of the words from the input. The output should output after sorting "
      "the key alphanumerically. ")


def __prompt():
    frequency = {}
    sentence = input("Please enter a sentence: ")
    list_of_words = sentence.split(" ")
    for i in list_of_words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    sort_orders = sorted(frequency.items(), key=lambda x: x[0], reverse=False)
    for i in sort_orders:
        print(i[0], i[1])


print(__prompt())

time.sleep(1)
# square a number
print("--------------------------------------------------------------------------------------------")
print("Write a method which can calculate square value of number")
user_input = int(input("Please enter a number to be squared: "))


def square(input_par):
    return input_par ** 2


print("The square of ", user_input, "is ", square(user_input))

time.sleep(1)
# docs
print("--------------------------------------------------------------------------------------------")
print("Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()")


def print_docs():
    print(abs.__doc__)
    print(int.__doc__)
    print(raw_input.__doc__)


print_docs()

time.sleep(1)
# define a class
print("--------------------------------------------------------------------------------------------")
print("Define a class, which have a class parameter and have a same instance parameter.")


class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("The Person you created is named: ", self.name, "and", self.age, "years old")


p1 = Person("Judy", 28)
p1.display()


class Student(Person):

    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_student(self):
        print("The Student you created is named: ", self.name, ",", self.age, "years old and is in section:",
              self.section)


s1 = Student("Peter", 22, "3-B")
s1.display_student()

time.sleep(1)
# sum
print("--------------------------------------------------------------------------------------------")
print("Define a function which can compute the sum of two numbers.")

par1 = int(input("Please enter the first number: "))
par2 = int(input("Please enter the second number: "))


def sum_of_numbers(input1, input2):
    return input1 + input2


print("The sum of the two numbers are :", sum_of_numbers(par1, par2))

time.sleep(1)
# conversion
print("--------------------------------------------------------------------------------------------")
print("Define a function that can convert a integer into a string and print it in console.")

int_input = int(input("Please enter any number: "))


def convert_int(input_par):
    return str(input_par)


print(int_input, "converted to a string is: ", convert_int(int_input))

time.sleep(1)
# sum of two strings
print("--------------------------------------------------------------------------------------------")
print("Define a function that can receive two integral numbers in string form and compute their sum and then print it "
      "in console.")

input_string1 = input("Please enter a number: ")
input_string2 = input("Please enter a number again: ")


def convert_strings_int(input_par1, input_par2):
    x = int(input_par1)
    y = int(input_par2)
    return x + y


print(input_string1, "+", input_string2, "=", convert_strings_int(input_string1, input_string2))

time.sleep(1)
# concat two strings
print("--------------------------------------------------------------------------------------------")
print("Define a function that can accept two strings as input and concatenate them and then print it in console.")

input_string1 = input("Please enter a string: ")
input_string2 = input("Please enter a string again: ")


def concat_strings(input_par1, input_par2):
    return input_par1 + input_par2


print("The concatenation of the two strings are:", concat_strings(input_string1, input_string2))


time.sleep(1)
# concat two strings
print("--------------------------------------------------------------------------------------------")
print("Define a function that can accept two strings as input and print the string with maximum length in console. If "
      "two strings have the same length, then the function should print al l strings line by line.")

input_string = input("Please enter a string: ")
input_string1 = input("Please enter a string again: ")


def print_maxlength(input_par, input_par1):
    if len(input_par) == len(input_par1):
        print("length is equal printing both")
        return input_par + " " + input_par1

    if len(input_par) > len(input_par1):
        return input_par
    else:
        return input_par1


print(print_maxlength(input_string, input_string1))


time.sleep(1)
# even or odd
print("--------------------------------------------------------------------------------------------")
print('Define a function that can accept an integer number as input and print the "It is an even number" if the '
      'number is even, otherwise print "It is an odd number".')

input_num = int(input("Please enter a number: "))


def even_or_odd(input_par):
    if input_par % 2 == 0:
        return "It is an even number"
    else:
        return "It is an odd number"


print(even_or_odd(input_num))

time.sleep(1)
# dictionary 1-3
print("--------------------------------------------------------------------------------------------")
print("Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and "
      "the values are square of keys.")


def dict_of_3():
    d = dict()
    for i in range(1, 4):
        d[x] = x ** 2
    print(d)


print(dict_of_3())


time.sleep(1)
# dictionary 1-20
print("--------------------------------------------------------------------------------------------")
print("Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and "
      "the values are square of keys.")


def dict_of_3():
    d = dict()
    for i in range(1, 21):
        d[x] = x ** 2
    print(d)


print(dict_of_3())


