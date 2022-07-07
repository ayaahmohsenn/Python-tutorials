##modules// gets functionf from other codes without having to copy it
#import L4
#print(L4.match_string("aya","aya"))

##classes and objects in python
class employee:
    def __init__(self, name, age, department, is_manager, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating = rating #rating from 1 to 5
        self.salary = salary

    def is_excellent(self):
         if self.rating >= 4.5:
             return True
         else:
             return False
    def bonus(self):
        if self.age == 60:
            self.salary +=500
            print("salary increased to " + str(self.salary))
        else:
            print("no bonus added, salary is still " + str(self.salary))


class doctor:
    def studied_years(self):
        print("I studied 7 years")

    def works_where(self):
        print("I work in a hospital")

    def paid_by_who(self):
        print("I get paid by government ")

#class inheretance
class FamilyDoctor(doctor):
    def what_specialization(self):
        print("I work with families")
#when u want to change the content of another inherited class overwrite it
    def paid_by_who(self):
        print("I get paid by people ")

