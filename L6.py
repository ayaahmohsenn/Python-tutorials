#2D lists

no_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(no_list[0][1])

#Nested loops

for row in no_list:
    for column in row:
        print(column)

#Try-except// used for avoiding errors in the code
try:
    value = int(input("Enter a number:"))
    print(value)
    x = 10/0
except ZeroDivisionError as err:
    print(err)

#except: #default except//has to be used at the end of ur program
except ValueError as err1:
    print(err1)
print("success")

## reading files
AyaFile = open("ayaaa.txt","r") #read can be w for write, a>> append,r+>>read+write
print(AyaFile.readable()) ##check if the file is readable
#print(AyaFile.read())  ##reads the whole file
print(AyaFile.readlines()[0])  #read all the lines and put them in a list
#print(AyaFile.readline())  #reads the first line
#print(AyaFile.readline())  #reads the second file
AyaFile.close()

AyaaFile = open("ayaaa.txt","r")
for aya in AyaaFile:
    print(aya)
AyaaFile.close()

#writing in files
#you can create new files using a, a+, w, and w+
AyFile = open("character.txt","a")
AyFile.write("\n This is a second line")
#FileName.writelines works on writing lines from a specific list -for exp- in ur file
AyFile.close()
