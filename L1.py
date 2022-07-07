print("Hello world")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
myname ="Aya" #string variable
mylastname="Mohsen"
myage = "23"
print("my name is "+myname) #concatenation
print("my age \n is "+myage)
print("code\"zilla")
print("my name is Aya \tand my age is 23")
print(myname)
#strings functions
print(myname.lower()) #makes ur sentence in small letters
print(myname.upper()) #makes ur sentence in capital letter
print(myname.isupper()) #check if ur sentence is capital
print(myname.islower()) #check if ur sentence is small
print(myname.upper().isupper()) #2 funcs simultaneously
print(myname.lower().islower())
print(len(myname)) #get the length of the string
myage = 23
print("name is %s"% myname)
print("age is %d" % myage)
print(myname[0]) #python start to count from zero
print(myname[1])
print(myname[0], mylastname[0])
print(myname.index("y"))
print(mylastname.index("sen")) #passing parameter to the function
print(mylastname.replace("s","z"))


