def hey(name, age):
    print("my name is" + name + "my age is" + str(age))


def hello(*values):
    print("helloo", "nikhil", "learn", "god")


value = "nikhil"
hey(value, 21)
hello()

value = 10  # global variable


def sample():  # function definition
    value = 30  # local variable
    print(value)


sample()  # function call
print(value)


def sample(num1, num2):
    sum = num1 + num2
    return sum


result = sample(12, 55)
print(result)
