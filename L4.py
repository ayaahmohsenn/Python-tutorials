##functions
def say_hi(name, age):
    print("Hello "+name+ " and ur age is "+age)  #identation is required in python

#calling the function
name = input("Enter ur name: ")
age = input("Enter ur age: ")
say_hi(name, age)

##functions with return statement
def cube(num):
    return num*num*num

##calling the func
cubedNum = cube(3)
print(cubedNum)

def sum(num1,num2):
    return num1+num2

##calling the func
print(sum(4,9))

#conditionals
is_hungry = True
want_to_eat = False

if is_hungry or want_to_eat:
    print("go eat!")
else:
    print("don't eat")


if is_hungry and want_to_eat:
    print("go eat!")
elif is_hungry and not want_to_eat:
    print("eat so u can survive")
elif not is_hungry and want_to_eat:
    print("don't eat obeisyy")
else:
    print("don't eat")


##comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(9, 13, 6))

def match_string(str1, str2):
    if str1==str2:
        print("strings match")
    else:
        print("strings don't match")

match_string("Aya", "Aya")
