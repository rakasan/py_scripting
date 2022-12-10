#optional parameters:

class person(object):
    population = 50
    def __init__(self,name, age):
        self.name = name
        self.age = age
    @classmethod #call it on any instance of a class
    def getPopulation(cls):
        return cls.population

    @staticmethod #same as class, but it does not need the class parameter
    def isAdult(age):
        return age > 18

    def display(self):
        print(self.name,' is ',self.age,'years old')

def func(x =1):
    return x **2

def func_2(word,freq=1):
    print(word*freq)


newPerson = person('vlad',18)

#call = func(5)
#call_2 = func_2('vlad',5)

#print(call)



