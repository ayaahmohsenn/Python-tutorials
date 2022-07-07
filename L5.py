## a calculator
num1 = float(input("Enter the first number: "))
operator = input("Please enter ur operator: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Wrong operator! Enter again! ")

#dictionaries// a list that every value in it corresponds to another value
convert_month = {    ##I cannot have 2 keys in the dictionary with the same name
    0 : "January",
    "Feb" : "February",
    "Mar" : "March",
}
print(convert_month.get(0))
print(convert_month.get("aya", "the value doesn't exist"))

##while loops
i = 1
while i <= 10:
    i += 1
    if i == 6:
        continue ##it can also be break
    print(i)
else:
    print("The loop has ended! ")

##for loops
for letter in "codezilla":
    print(letter)

buddies = ["aya", "radwa", "toka", "ahmed", "krema"]
for buddy in buddies:
    print(buddy)

for x in range(10):   #prints numbers from 0 to 10 excluding 10
    print(x)

for x in range(5,20):   #prints numbers from 5 to 20 excluding 20
    print(x)

for x in range(len(buddies)):
    print(buddies[x])

for y in range(10):
    if y % 2 == 0:
        print(y, "is an even number! ")

for buddy in range(len(buddies)):
    if buddies[buddy] == "toka":
        print(buddies[buddy], "is the success")
        break #break the loop after the code finds toka in the list buddies
    else:
        print(buddies[buddy], "is happy")

# Power function
def power(baseNum,PowNum):
    result = 1
    for index in range(PowNum):
        result = result * baseNum
    return result

print(power(3,2))
