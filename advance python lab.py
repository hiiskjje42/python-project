#!/usr/bin/env python
# coding: utf-8

# # 1

# # Write a program illustrating class definition and accessing class members.

# In[1]:


class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
#create object
obj=Student("xyz",34,78)
print("Name is:",obj.name)
print("Age is:",obj.age)
print("Marks is:",obj.marks)


# # 2

# # Write a program to implement default constructor, parameterized constructor, and destructor.

# In[2]:


class Student:
    def __init__(self,name,age): # parametrized constructor
        print("object created in student1")
        self.name=name
        self.age=age
    def __del__(self):
        print("object destroyed in student1")
class student2:
    def __init__(self): # default constructor 
        print("object created in student2")
        self.name="vikas"
        self.age=56
    def __del__(self):
        print("object destroyed in student2")
obj=Student("vinay",34)
obj2=student2()
print("Information of student1 is")
print("Name is:",obj.name)
print("age is",obj.age)
print("Information of student2 is")
print("Name is:",obj2.name)
print("age is",obj2.age)
obj=90
obj2=67


# # 3

# # Create a Python class named Rectangle constructed by a length and width.

# # a.Create a method called area which will compute the area of a rectangle.

# In[1]:


class Rectangle(object):
    def __init__(self):
        self.length=int(input("enter length"))
        self.width=int(input("enter width"))
    def area(self):
        return self.length*self.width
obj=Rectangle()
print(obj.area())


# # 4

# # Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).

# # a. Write an instance method called add which returns the sum of the attributes x and y. 

# # b. Write a class method called multiply, which takes a single number parameter a and returns the product of a and MULTIPLIER.

# # c. Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.

# # d. Write a method called value which returns a tuple containing the values of x and y.

# In[2]:


class Number:
    MULTIPLIER=2
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #instance method
    def add(self):
        return self.x+self.y
    #class method
    @classmethod
    def multiply(cls,a):
        return a*cls.MULTIPLIER
    #static method
    @staticmethod
    def subtract(b,c):
        return b-c
    #instance method
    def value(self):
        return self.x,self.y
num=Number(3,4)
print(num.add())
print(num.multiply(3))
print(num.subtract(56,78))
print(num.value())


# # 5

# # Create a class named as Student to store the name and marks in three subjects.Use List to store the marks. 

# # a. Write an instance method called compute to compute total marks and average marks of a student.

# # b. Write a method called display to display student information.

# In[4]:


class Student:
    def __init__(self):
        self.name=input("enter name of student")
        self.marks=input("enter three subject marks separated by space").split()
    def compute(self):
        self.total=0
        for i in self.marks:
            self.total+=int(i)
        self.avg=self.total/3
    def display(self):
        print("Name:",self.name)
        print("Total marks:",self.total)
        print("Averge is:",self.avg)
stud=Student()
stud.compute()
stud.display()


# # 6

# # Create a class Employee that keeps a track of the number of employees in an organization and also stores their name, designation and salary details.

# # a. Write a method called getdata to take input (name, designation, salary) from user

# # b. Write a method called average to find average salary of all the employees in the organization.

# # c. Write a method called display to print all the information of an employee.

# In[4]:


class Employee(object):
    total_salary=0
    count=0
    def getdata(self):
        print("enter details of Employee",Employee.count+1)
        self.name=input("Enter name")
        self.desi=input("Enter designation")
        self.salary=int(input("Enter salary"))
        Employee.total_salary+=self.salary
        Employee.count+=1
    @classmethod
    def avg(cls):
        return cls.total_salary/cls.count
    def display(self):
        print(f"{self.name}\t{self.desi}\t{self.salary}")
        
e1=Employee()
e2=Employee()
e3=Employee()
for i in (e1,e2,e3):
    i.getdata()
print("Details of all Employee are")
print("Name\tdesi\tsalary")
for i in (e1,e2,e3):
    i.display()
print("average salary is",Employee.avg())


# # 7

# # Create a Python class named Circle constructed by a radius. Use a class variable to define the value of constant PI. 

# # a. Write two methods to be named as area and circum to compute the area and the perimeter of a circle respectively by using class variable PI. 

# # b. Write a method called display to print area and perimeter

# In[10]:


class Circle:
    PI=3.14
    def __init__(self,r):
        self.r=r
        
    def area(self):
        self.A=Circle.PI*self.r*self.r
        
    def circum(self):
        self.pari=2*Circle.PI*self.r
        
    def display(self):
        print("area is:",self.A)
        print("circumference is:",self.pari)
        
cir=Circle(4)
cir.area()
cir.circum()
cir.display()


# # 8

# # Create a class called String that stores a string and all its status details such as number of uppercase letters, lowercase letters, vowels ,consonants and space in instance variables.

# # a. Write methods named as count_uppercase, count_lowercase, count_vowels, count_consonants and count_space to count corresponding values.

# # b. Write a method called display to print string along with all the values computed by methods in (a).

# In[13]:


class String:
    def __init__(self):
        self.string=input("Enter string")
        self.uppercase=0
        self.lowercase=0
        self.vowels=0
        self.consonants=0
        self.space=0
    def count_uppercase(self):
        for i in self.string:
            if ord(i)>=65 and ord(i)<=90:
                self.uppercase+=1
    def count_lowercase(self):
        for i in self.string:
            if ord(i)>=97 and ord(i)<=122:
                self.lowercase+=1
    def count_vowel(self):
        for i in self.string:
            if i in 'AEIOUaeiou':
                self.vowels+=1
    def count_consonants(self):
        for i in self.string:
            if i not in 'AEIOUaeiou':
                self.consonants+=1
    def count_space(self):
        for i in self.string:
            if i==' ':
                self.space+=1
    def display(self):
        print("string is",self.string)
        print("count uppercase is",self.uppercase)
        print("count lowercase is",self.lowercase)
        print("count vowel is",self.vowels)
        print("count consonants is",self.consonants)
        print("count space is",self.space) 
        
stri=String()
stri.count_uppercase()
stri.count_lowercase()
stri.count_vowel()
stri.count_consonants()
stri.count_space()
stri.display()


# # 9

# # Write a program that has a class called Fraction with attributes numerator and denominator.

# # a. Write a method called getdata to enter the values of the attributes.

# # b. Write a method show to print the fraction in simplified form.

# In[4]:


class Fraction:
    def __init__(self):
        self.nun=None
        self.demo=None
    def getdata(self):
        self.num=int(input("enter numerator"))
        self.demo=int(input("enter denominator"))
        
    def simplify(self):
        gcd=self.GCD()
        self.num//=gcd
        self.demo//=gcd
        
    def GCD(self):
        x=self.num
        y=self.demo
        rem=x%y
        while rem:
            x=y
            y=rem
            rem=x%y
        return y
    def show(self):
        print(f"{self.num}/{self.demo}")
f1=Fraction()
f1.getdata()
print("num is")
f1.show()
f1.simplify()
print("simplified form is")
f1.show()


# # 10

# # Write a program that has a class Numbers with a list as an instance variable.

# # a. Write a method called insert_element that takes values from user. 

# # b. Write a class method called find_max to find and print largest value in the list.

# In[12]:


class Numbers:
    def __init__(self):
        self.num=[]
    def insert_element(self,n):
        print("insert element in the list")
        for i in range(n):
            self.num.append(int(input()))
    @classmethod                      
    def find_max(cls,self):
        max=None
        for i in self.num:
            if max is None or max<i:
                max=i
        return max
num=Numbers()
n=int(input("enter limit of number of elements in the list"))
num.insert_element(n)
print("max is :",Numbers.find_max(num)) 


# # 11

# # Write a program that has a class Point with attributes x and y.

# # a. Write a method called midpoint that returns a midpoint of a line joining two points.

# # b. Write a method called length that returns the length of a line joining two points.

# In[3]:


import math
class Point:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y
    def midpoint(self,other):
        mid=Point()
        mid.x=(self.x+other.x)/2
        mid.y=(self.y+other.y)/2
        return mid
    def length(self,other):
        length=math.sqrt((other.x+self.x)**2+(other.y+self.y)**2)
        return length
p1=Point(2,4)
p2=Point(5,6)
p3=p1.midpoint(p2)
print(f"({p3.x},{p3.y})")
print(f"length is {p1.length(p2)}")


# # 12

# # Create a class called Complex. Write a menu driven program to read, display, add and subtract two complex numbers by creating corresponding instance methods.

# In[1]:


class Complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def read(self):
        self.real=int(input("Enter real part"))
        self.imag=int(input("Enter imaginary part"))
    def add(self,other):
        complex1=Complex()
        complex1.real=self.real+other.real
        complex1.imag=self.imag+other.imag
        return complex1
    def sub(self,other):
        complex2=Complex()
        complex2.real=self.real-other.real
        complex2.imag=self.imag2other.imag
        return complex2
    def display(self):
        print(f"{self.real}+{self.imag}j")
ch='y'
while ch=='y':
    print("************Enter 1. For read operation")
    print("************Enter 2. For disply operation")
    print("************Enter 3. For add operation")
    print("************Enter 4. For sub operation")
    choice=int(input())
    if choice==1:
        result=Complex()
        result.read()
    elif choice==2:
        try:
            result=display()
        except:
            print("First read number")
    elif choice==3:
        print("Enter two complex number")
        com=Complex()
        com.read()
        com2.Complex()
        com2.read()
        result=Complex()
        result=Com.add(com2)
        print("result is")
        result.display()
    elif choice==4:
        print("Enter two complex number")
        com=Complex()
        com.read()
        com2.Complex()
        com2.read()
        result=Complex()
        result=Com.sub(com2)
        print("result is")
        result.display()
    else:
        print("Error")
    print("Do you want continue press y")
    ch=input()
print("Thank you")       


# # 13

# # Write a Program to illustrate the use of _str(), __repr(), __new, __doc_, _dict, __name_ and _bases_ methods.

# In[19]:


class Demo(object):
    "this is demo class"
    value=10
    def __init__(self,name):
        self.name=name
print(Demo.__doc__)
print(Demo.__dict__)
print(Demo.__name__)
print(Demo.__bases__)
print(Demo.)


# # 14

# # Create a BankAccount class. Your class should support the following methods: 

# # a. __init__(self, account_no).

# # b. deposit (self, account_no, amount). 

# # c. withdraw (self, account_no, amount).

# # d. get_balance (self, account_no).

# In[2]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance  ")
    def display(self):
        print("Net Available Balance=",self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()


# # 15

# # Write a program to illustrate the use of following built-in methods:

# # a. hasattr(obj,attr).

# # b. getattr(object, attribute_name [, default]).

# # c. setattr(object, name, value).

# # d. delattr(class_name, name).

# In[22]:


class ABC:
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is =",self.var)
obj=ABC(10)
obj.display()
getattr(obj,"var")
setattr(obj,"var",56)
obj.display()
setattr(obj,"num",23)
print(obj.__dict__)
delattr(obj,"num")
print(obj.__dict__)
print(hasattr(obj,"var"))


# # 16

# # Write a program to create class Employee. Display the personal information and salary details of 5 employees using single inheritance.

# In[1]:


class Employee:
    def __init__(self):
        self.name=input("Enter name")
        self.profile=input("Enter profile")
        self.salary=int(input("Enter salary"))
class Personal(Employee):
    def display(self):
        print(f"Name:{self.name},profile:{self.profile},salary:{self.salary}")
obj=[]
for i in range(5):
    print(f"Data of Employee{i+1}")
    obj.append(Personal())
for i in range(5):
    obj[i].display()


# # 17

# # WAP that extends the class Employee. Derive two classes Manager and Team Leader from Employee class. Display all the details of the employee working under a particular Manager and Team Leader.

# In[18]:


class Employee:
    def __init__(self,data):
        self.data=data
    def display_manager(self):
        for i in self.data:
            if "mn" in i[3]:
                print(i)
    def display_team_leader(self):
        for i in self.data:
            if "tl" in i[3]:
                print(i)
class Manager(Employee):
    def display_manager(self):
        Employee.display_manager(self)
        
class Team_leader(Employee):
    def display_Team_Leader(self):
        Employee.display_team_leader()   
        
emp=[['emp1',25,'developer','mn123'],['emp2',30,'tester','tl1223']]
obj= Manager(emp) 
print('Employee Under Manager')
obj.display_manager() 
obj1=Team_leader(emp) 
print('Employee Under Team Leader')
obj1.display_team_leader()     


# # 18

# # Write a program that has a class Point. Define another class Location which has two objects (Location and destination) of class Point. Also, define a function in Location that prints the reflection on the y-axis.

# In[7]:


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Location:
    def __init__(self,x1,y1,x2,y2):
        self.location=Point(x1,y1)
        self.destination=Point(x2,y2)
    def display(self):
        print("Location point:",self.location.x,self.location.y)
        print("Destination point:",self.destination.x,self.destination.y)
    def refection(self):
        self.destination.x=self.destination.x
        print("Reflection of destination is:",self.destination.x,self.destination.y)
loc=Location(1,2,3,4)
print(loc.display())


# # 19

# # WAP that create a class Student having attribute as name and age and Marks class inheriting Students class with its own attributes marks1, marks2 and marks3 as marks in 3 subjects. Also, define the class Result that inherits the Marks class with its own attribute total. Every class has its own display() method to display the corresponding details. Use __init__() and super() to implement the above classes.

# In[1]:


class student:
    def __init__(self):
        self.name=input("Enter Name")
        self.age=input("Enter age")
    def display(self):
        print("Name: ",self.name)
        print("age",self.age)
class Marks(student):
    def __init__(self):
        super().__init__()
        self.mark1=int(input("enter marks of first subject"))
        self.mark2=int(input("enter marks second subject"))
        self.mark3=int(input("enter marks of third subject"))
    def display(self):
        super().display()
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)
class Result(Marks):
    def __init__(self):
        super().__init__()
        self.total=self.mark1 + self.mark2 + self.mark3
    def display(self):
        super().display()
        print("Resultant total is",self.total)
res=Result()
res.display()


# # 20

# # Write a program that create a class Distance with members km and metres. Derive classes School and office which store the distance from your house to school and office along with other details.

# In[1]:


class Distance:
    def __init__(self,km=None,metre=None):
        self.km=km
        self.metre=metre
class School(Distance):
    def Details(self):
        self.Location=input("Enter location of school:")
        self.km=int(input("Enter distance in km/metre,km--->"))
        self.metre=int(input("Metre---->"))
    def display(self):
        print(f"Location:({self.Location}\n diatance between school and house:{self.km}km{self.metre}m)")  
class office(Distance):
    def Details(self):
        self.Location=input("Enter location of office:")
        self.km=int(input("Enter distance in km/metre,km--->"))
        self.metre=int(input("Metre---->")) 
    def display(self):
        print(f"Location:({self.Location}\n diatance between office and house:{self.km}km{self.metre}m)") 
sch=School()
ofc=office()
for i in (sch,ofc):
    i.Details()
for i in (sch,ofc):
    i.display()


# # 21

# # Write a program to create an abstract class Vehicle. Derive three classes Car, Motorcycle and Truck from it. Define appropriate methods and print the details of vehicle.

# In[4]:


from abc import ABC,abstractclassmethod
class vechile(ABC):
    def __init__(self,name):
        print("Details of",name)
    @abstractclassmethod
    def getDetails(self):
        pass
class Car(vechile):
    def getDetails(self):
        self.Name="Dzire"
        self.model1=2020
        self.model="Automatic"
    def display(self):
        print("Name:",self.Name)
        print("model1",self.model1)
        print("model",self.model)
class Motorcycle(vechile):
    def getDetails(self):
        self.Name="Bajaj"
        self.model1=2021
        self.model="Manual"
    def display(self):
        print("Name:",self.Name)
        print("model1",self.model1)
        print("model",self.model)
class Truck(vechile):
    def getDetails(self):
        self.Name="Ashoka"
        self.model1=2021
        self.model="Manual"
    def display(self):
        print("Name:",self.Name)
        print("model1",self.model1)
        print("model",self.model)
car=Car("car")
car.getDetails()
car.display()
moto=Motorcycle("Motorcycle")
moto.getDetails()
moto.display()
truck=Truck("Truck")
truck.getDetails()
truck.display()


# # 22

# # Write a program that has a class Polygon. Derive two classes Rectangle and triangle from polygon and write methods to get the details of their dimensionsand hence calculate the area.

# In[1]:


class Polygon:  
    def __init__(self,name):
        self.name=name
    def getdetails(self):
        print(f"enter details of {self.name}")
    def area(self):
        print(f"area of {self.name}")
class Rectangle(Polygon):
    def getdetails(self):
        super().getdetails()
        self.length=int(input("enter length"))
        self.width=int(input("enter width"))
    def area(self):
        super().area()
        return self.length*self.width 
class Triangle(Polygon):
    def getdetails(self):
        super().getdetails()
        self.base=int(input("enter base"))
        self.height=int(input("enter height"))
    def area(self):
        super().area()
        return 0.5*self.base*self.height
rec=Rectangle("Rectangle")
tri=Triangle("Triangle")
rec.getdetails()
print(rec.area())
tri.getdetails()
print(tri.area())


# # 23

# # Write a program that extends the class Shape to calculate the area of a circle and a cone .(use super to inherit base class methods)

# In[3]:


from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,r,l=None):
        self.r=r
        self.l=l
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def area(self):
        self.A=3.14*self.r*self.r
        print("area is",self.A)
class cone(shape):
    def area(self):
        self.A=3.14*self.r*(self.r+self.l)
        print("area is",self.A)
cir=circle(3)
cir.area()
con=cone(3,4)
con.area()


# # 24

# # Write a program to demonstrate hybrid inheritance and show MRO for each class.

# In[8]:


class Class1:
    def m(self):
        print("In Class1")
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")  
        super().m() 
print(Class4.mro())


# # 25

# # Write a program to overload + operator to add to fraction object of fraction class which contain two instance variable numerator and denominator. Also, define the instance method simplify() to simplify the fraction objects.

# In[21]:


def GCD(num,dem):  
    rem = num%dem
    while rem:
        num,dem=dem,rem
        rem=num%dem
    return dem
class Fraction:
    def __init__(self,num=None,dem=None):
        self.num = num
        self.dem = dem
    def __mul__(self,other):
        f3 = Fraction()
        f3.num = self.num*other.num
        f3.dem = self.dem*other.dem
        return f3
    def simplify(self):   
        gcd = GCD(self.num,self.dem)
        self.num//=gcd
        self.dem//=gcd
    def __str__(self):
        return f"{self.num}/{self.dem}"

f1 = Fraction(6,9)
print(f1)
f2 = Fraction(5,6)
print(f2)
f3 = f1*f2
print(f"The Result is: {f3}")


# # 26

# # Write a program to compare two-person object based on their age by overloading > operator.

# In[12]:


class person:
    def __init__(self,age):
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
vikash=person(34)
nitin=person(45)
if nitin>vikash:
    print("nitin is greater than vikash")
else:
    print("vikash is grater than nitin")


# # 27

# # Write a program to overload inoperator.

# In[18]:


class Example:
    def __init__(self,*lst):
        self.item=lst
    def __contains__(self,other):
        if other in self.item:
            return "success"
        else:
            return "not success"    
obj=Example(12,34,56,7,8,90)
if 56 in obj:
    print("success")
else:
    print("not success")


# # 28

# # WAP to create a Complex class having real and imaginary as it attributes.Overload the +,-,/,* and += operators for objects of Complex class.

# In[9]:


class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


# # 29

# # Write a program to inspect the object using type() ,id(), isinstance(), issubclass() and callable() built-in function.

# In[69]:


#type()
import sys
def fun():
    pass
class myobject(object):
    def __init__(self):
        pass
    def inst(self):
        pass
class demo(myobject):
    pass
obj=myobject()
print(type(obj))
#id()
print(id(sys))
#isinstance()
print(isinstance(obj,myobject))
print(isinstance(obj,object))
print(isinstance('2',int))
#issubclass()
print(issubclass(object,object))
print(issubclass(object,myobject))
print(issubclass(demo,myobject))
print(issubclass(demo,object))
#callable()
print(callable(fun))
print(callable(obj.inst))
print(callable(myobject))
print(callable(1))


# # 30

# # WAP to inspect the program code using the functions of inspect module.

# In[31]:


import inspect
class A(object):
    pass
print(inspect.isclass(A))


# # 31

# # Write a program to create a new list containing the first letters of every element in an already existing list.

# In[28]:


def firstLetterWord(str):
    result = ""
    v = True
    for i in range(len(str)):
        if (str[i] == ' '):
            v = True
        elif (str[i] != ' ' and v == True):
            result += (str[i])
            v = False
    return result
if __name__ == "__main__":
    str = "advance python lab"
    print(firstLetterWord(str))


# # 32

# # Write a program using reduce() function to calculate the sum of first 10 natural numbers.

# In[72]:


from functools import reduce
list2 = [1,2,3,4,5,6,7,8,9,10]
fins = reduce(lambda x,y:x+y,list2)
print(fins)


# # 33

# # Write a program that convert a list of temperatures in Celsius into Fahrenheit using map() function.

# In[1]:


Celsius=[26.2,33.2,29,32.4]
Fahrenheit=map(lambda x:(float(9)/5)*x+32,Celsius)
print(list(Fahrenheit))


# # 34

# # Write a program that creates an iterator to print squares of numbers.

# In[1]:


def printSquares(n):
    square = 0; prev_x = 0
    for x in range(0, n):
        square = (square + x + prev_x)
        print(square, end = " ")
        prev_x = x
n = 5;
printSquares(n);


# # 35

# # Write a program that create a custom iterator to create even numbers.

# In[5]:


start = int (input ("Enter the start of range: "))
end = int (input ("Enter the end of range: "))
for num in range (start, end + 1):
    if num % 2 == 0:
        print (num, end = " ")


# # 36

# # Write a program to create a generator that starts counting from 0 and raise an exception when counter is equal to 10.

# In[2]:


def numberGenerator():
    num=0
    while num<10:
        yield num
        num+=1
    if num==11:
        raise OverflowError
obj=numberGenerator()
for i in obj:
    print(i)


# # 37

# # Write a program to create a generator to print the Fibonacci number.

# In[2]:


def fibonacciGenerator():
    a=0
    b=1
    for i in range(6):
        yield b
        a,b= b,a+b
obj = fibonacciGenerator()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


# # 38

# # Write a program to create an arithmetic calculator using tkinter.

# In[10]:


from tkinter import *
root=Tk()
root.title("Simple Calculator")
# creating main frame
mainframe=Frame(root,width=45,bd=10,relief=RIDGE,bg="blue")
mainframe.pack()
inner=Frame(mainframe,width=45,bd=10,relief=RIDGE,bg="black")
inner.pack()
e=Entry(inner,width=65,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=1)
def onclick(num):
    x=e.get()
    e.delete(0,END)
    e.insert(0,str(x)+str(num))
def clear():
    e.delete(0,END)
def add():
    global first,op
    op='+'
    first=e.get()
    e.delete(0,END)
def sub():
    global first,op
    op='-'
    first=e.get()
    e.delete(0,END)
def mul():
    global first,op
    op='*'
    first=e.get()
    e.delete(0,END)  
def div():
    global first,op
    op='/'
    first=e.get()
    e.delete(0,END)
def equal():
    second=e.get()
    if op=='+':
        result=float(first)+float(second)
    elif op=='-':
        result=float(first)-float(second)
    elif op=='*':
        result=float(first)*float(second)
    elif op=='/':
        result=float(first)/float(second)
    e.delete(0,END)
    e.insert(0,result)
############################################################
 ####Button widget####
button_1=Button(inner,text='1',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(1))
button_2=Button(inner,text='2',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(2))
button_3=Button(inner,text='3',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(3))
button_4=Button(inner,text='4',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(4))
button_5=Button(inner,text='5',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(5))
button_6=Button(inner,text='6',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(6))
button_7=Button(inner,text='7',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(7))
button_8=Button(inner,text='8',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(8))
button_9=Button(inner,text='9',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(9))
button_0=Button(inner,text='0',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=lambda:onclick(0))
# operation button
button_add=Button(inner,text='+',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=add)
button_sub=Button(inner,text='-',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=sub)
button_mul=Button(inner,text='*',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=mul)
button_div=Button(inner,text='/',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=div)
button_equal=Button(inner,text='=',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=equal)
button_clear=Button(inner,text='C',padx=30,pady=10,relief=RIDGE,font=15,width=4,command=clear)
#####place the number button######
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1)
root.mainloop()


# # 39

# # Write a program to draw colored shapes (line, rectangle, oval) on canvas.

# In[11]:


from tkinter import * 
from tkinter.ttk import * 
class Shape:
    def __init__(self, master = None):
        self.master = master
        self.create()
    def create(self):
        self.canvas = Canvas(self.master)
        self.canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "white", width = 2)
        self.canvas.create_oval(110, 10, 210, 80, outline = "red", fill = "green", width = 2)
        self.canvas.create_rectangle(230, 10, 290, 60, outline = "black", fill = "blue", width = 2)
        self.canvas.create_arc(30, 200, 90, 100, start = 0, extent = 210, outline = "green", fill = "red", width = 2)
        points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
        self.canvas.create_polygon(points, outline = "blue", fill = "orange", width = 2)
        self.canvas.pack(fill = BOTH, expand = 1)
if __name__ == "__main__":
    master = Tk()
    shape = Shape(master)
    master.title("Shapes")
    master.geometry("300x250+300+300")
    mainloop()


# # 40

# # Write a program to create a window that disappears automatically after 5 seconds.

# In[12]:


from tkinter import *
root=Tk()
def WaitAndClose():
    global root
    #close root after a five seconds
Button(root, text='Close', command=WaitAndClose).pack()
mainloop()


# # 41

# # Write a program to create a button and a label inside the frame widget. Button should change the color upon hovering over the button and label should disappear on clicking the button.

# In[13]:


from tkinter import *  
from tkinter.ttk import *
root = Tk()            
root.geometry('100x100')
btn = Button(root, text = 'Click me !',
                command = root.destroy)
btn.pack(side = 'top')
root.mainloop()


# # 42

# # Write a program to create radio-buttons (Male, Female, and Transgender) and a label. Default selection should be on Female and the label must display the current selection made by user.

# In[14]:


import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
tk.Label(root, 
        text="Label",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
               text="nitin",
               padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="kriti",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)
root.mainloop()


# # 43

# # Write a program to display a menu on the menu bar.

# In[15]:


import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
win = tk.Tk()  
win.title("Python GUI App")   
def _quit():  
    win.quit()  
    win.destroy()  
    exit()   
menuBar=Menu(win)  
win.config(menu=menuBar)
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="New")  
fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)    
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpMenu)    
win.mainloop()


# # 44

# # Write a NumPy program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.

# In[9]:


import numpy as np
x= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(x)


# # 45

# # Write a NumPy program to compute the multiplication of two given matrixes.

# In[2]:


import numpy as np
A=np.array([[2,0,1],[4,3,8],[9,8,7]])
B=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(A.dot(B)) #or
print(A@B)#or
print(np.matmul(A,B))


# # 46

# # Write a Program to create a series from a list, numpy array and dict.

# In[6]:


import pandas as pd
import numpy as np
lst=['h','i','i']
s= pd.Series(lst)
dct={'h':1,'e':2,'l':3,'l':4,'o':5}
s2=pd.Series(dct)
arr=np.array(['b','y','e'])
s3=pd.Series(arr)
print(s)
print(s2)
print(s3)


# # 47

# # Write a Program to convert a numpy array to a dataframe of given shape.

# In[7]:


nparray=np.array([['Aryan','adiba','sachin'],[30,34,56],[98,78,67]])
df=pd.DataFrame(nparray,index=['Name','Rollno','marks'],columns=['Id1','Id2','Id3'])
df


# # 48

# # Write a program to count number of missing values in each column.

# In[8]:


import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
df=pd.DataFrame({
'ord_no':[70001,np.nan,70002,np.nan,70005,np.nan],
'purch_amt':[65.26,5760,1983.43,250.45,75.29,3045.6],
'ord_date': [np.nan,'2012-08-17','2012-07-27','2012-10-10','2012-08-17','2012-04-25'],
'customer_id':[3003,3002,3001,3001,3004,3002],
'salesman_id':[np.nan,5002,5001,np.nan,5002,np.nan]})
print("Original Orders DataFrame:")
print(df)
print("Number of missing values of the said dataframe:")
print(df.isna().sum())


# # 49

# # Write a program to replace missing values in a column of a dataframe by the mean value of that column.

# In[7]:


import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
df=pd.DataFrame({
'ord_no':[70001,np.nan,70005,np.nan,np.nan,70013],
'purch_amt':[150.5,np.nan,948.5,1983.43,np.nan,3045.6],
'sale_amt':[10.5,np.nan,98.5,19.43,np.nan,75.29],
'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3001,3004],
'salesman_id':[5002,5003,5001,np.nan,5001,np.nan]})
print("Original Orders DataFrame:")
print(df) 
print("Replace the missing values with the most frequent values present in each column:")
result = df.fillna(df.mode().iloc[0])
print(result)


# # 50

# # Write a Pandas program to create a line plot of the opening, closing stock prices of Alphabet Inc. between two specific dates. Use the alphabet_stock_data.csv file to extract data.

# In[1]:


import pandas as pd


# In[2]:


cd C:\Users\Amritanshu sharma\Desktop


# In[3]:


pwd


# In[4]:


pd.read_csv("alphabet_stock_data.csv")


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df2 = df.loc[new_df]
plt.figure(figsize=(10,10))
df2.plot(x='Date', y=['Open', 'Close']);
plt.suptitle('Opening/Closing stock prices of Alphabet Inc.,\n 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.xlabel("Date",fontsize=12, color='black')
plt.ylabel("$ price", fontsize=12, color='black')
plt.show()


# In[ ]:




