# Initiate with python3.7 intro.py

class Person:
    def __init__(self, name, school, age):
        # data types - String, Numbers, List, Tuple, Dictionary
        # variables
        self.name = name
        self.school = school
        self.age = age
        self.marks = []
        # list can be changed
        self.list = ['soccer', 'swimming', 'badminton', 'listening music', 'sleeping']
        # tuple cannot be changed
        self.number_list = [13,29,18,1,8,22,21]
        self.tuple = ('singaporean', 's8273737')
        # set unique and unordered
        self.set = {1,2,5,6,6,7,7,7,7,8,8}
        # dictionary
        self.dict = { 'country': 'SG', 'postal': 120202 }

        # function without parameter
    def showList(self):
        print(self.name, self.age, self.list, self.tuple, self.set, self.dict)

        # function with parameter
    def setName(self, name):
        print('Hi. My name is {}'.format(name))

        # if elif else conditional statement
    def if_func(self, name):
        if name == 'John':
            print('John is a bad match')
        elif name == 'Eric':
            print('Eric is a good match')
        else: 
            print('I got no idea')

        # function with *args
    def sumNumbers(self, *args):
        return sum(args)

        # function with **kwargs
    def showNames(self, **kwargs):
        print(kwargs)

    def countNumbers(self, numOne, numTwo = 10):
        return numOne + numTwo

    def friend(self, friend_name): 
        return Person(friend_name, self.school, self.age)

    @staticmethod
    def staticFunc():
        print('static method')

    @classmethod
    def cls_friend(cls, origin, friend_name):
        return cls(friend_name, origin.school, origin.age, origin.prefect)

   # KIV Lambda function
    def lambda_func(self):
        res = lambda x: x * 2, self.number_list
        print(res)

    # KIV Class Method
    @classmethod
    def classFunc(cls, person):
        # return Person(person.name + '- says Hi')
        return cls(person.name + '- says Hi')

# Inheritance
class Child(Person):
    def __init__(self, name, school, age, prefect):
        super().__init__(name, school, age)
        self.prefect = True

sally = Person('Sally', 'amkss', 22)
sally.if_func('Eric')
print(sally.countNumbers(52))
print(sally.sumNumbers(10,12,22,23,25,1000))
sally.showNames(title='manager', role='administrative')
sally.lambda_func()

ivy = sally.friend('Ivy')
print(ivy.name)
print(ivy.age)

# using class method
eric = Child("Eric", 'Tpyss', 18, True)
print(eric.school)

jack = Child.cls_friend(eric, "Jack")
print(jack.name)
print(jack.school)

my_list = [22, 25, 26, 12, 11, 33]

def less_than_twenty(x):
    return x < 20

# Lambda Function
print(list(filter(less_than_twenty, my_list)))

# List Comprehension 
print([x for x in my_list if x < 20])



