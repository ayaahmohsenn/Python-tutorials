#lists in python
randoms = ["radwa", 1,8000, True, False, [1,"Aya", False]]
print(randoms)
print(randoms[2])
print(randoms[0])
names = ["aya"," radwa", "toka", "ahmed"]
print(names[-1]) #print the last value in the array
print(names[-2])
print(names[1:3]) #doesnt include index 3, just 1 and 2 in the array
print(names[0:2])
names[1] = "karima" #replace element in the array
print(names[1:]) #prints from index 1 to the end of the list
ages = ["23","52","19","8"]
print(names, ages)
names.extend(ages) #concatenation of 2 arrays using "extend" function
names += ages #another way of concatenation
print(names)
names.append("mohsen") #adding element to an array to the end
print(names)
names.insert(0, "hana") #adding element to an array in a specific position
print(names)
names.remove("hana") #removing an element from the array
print(names)
#names.clear() #removing entire array
poppp = names.pop() #the last element in the array
print(poppp)

print(names.index("aya"))
print(names.count("aya")) #tells you how many times "aya" is repeated in the array
names.sort()
print(names) #sort the array alphabitcally and ascending
names_new = names.copy()
print(names_new) #shallow copy


#Tuples// tuples cannot be changes after it constructed
coordinates = (15,25)
list_of_tuples = [(13,24),(18,16),(20,1)]
print(coordinates[0])
print(list_of_tuples)
