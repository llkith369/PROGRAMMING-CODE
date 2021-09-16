from datetime import date
from os import access
from types import ModuleType



"""Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""

#camel case in this case except 1st letter it should start with capital letter 
myJarvis = 'AI COMPUTER camel case'
print(myJarvis)

#pascal case  in this case all letters must start with capital letters
MyJarvis = 'AI COMPUTER pascal case'
print(MyJarvis)

#snake case in this case there should be gap with symbol (_)in between words
my_jarvis = 'AI COMPUTER snake case'
print(my_jarvis)
  

#multiple variable declaration in a line 
l,i,k,i, = "likith","AI","computer","jarvis 1.0"
print(l)
print(i)
print(k)
print(i)

#multiple variable with same value 
A=B=C= "JARVIS"
print(A)
print(B)
print(C)

#unpacking a collection 
courses = ["java","python","AI"]    #use ("") or ('') for declaration
d,e,f = courses
print(d)
print(e)
print(f)

#output variables 
#adding variables 
D = "future"
print("AI is "+D)

#few examples on adding
E = 'likith'
F = 'meruvu'
print(E+F)

#ex-2
g = 200
f = 56
print(g+f)

#ex-3
G = 300
F = 69
sum = G+F
print(sum)

#global variables
''' you are giving an extra value to x and y by using global variable of each variable in the function as we used x and y in top of the programs'''

def myfunc():
  global x
  x = " is future trend"

  global y
  y = "artificial intelligence"  
  print(y+x)

myfunc()

print(myfunc)

#data types
#integer data type
x = 5
print(type(x))
print(x)

#string data type 
#it must contain ("") in declared values
x = "python"
print(type(x))
print(x)

#float data type
x = 5.0
print(type(x))
print(x)

#complex data type
x = 5j
print(type(x))
print(x)

#list data type 
x = ["banana","apple","grapes"]
print(type(x))

#tuple data type
x = ("scarl","m416","groza")
print(type(x))
print(x)

#range data type
x = range(369)
print(type(x))
print(x)

#dict data type
x = {"name": "likith", "age":18}
print(type(x))
print(x)

#set data type 
x = {"AI","jarvis","python"}
print(type(x))
print(x)

#frozenset data type
x = frozenset({"AI","jarvis","python"})
print(type(x))
print(x)

#boolean data type
x = False     #same for true statements
print(type(x))
print(x)

#binary data types
x = b"5"     #bytes data type 
print(type(x))
print(x)

#bytes array
x = bytearray(100)
print(type(x))
print(x)

#memory view data types
x = memoryview(bytes(10))
print(type(x))
print(x)

#type conversion
x = float(-3578)
y = int(2.0007)
z = complex(y)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#random module 
import random
print("20Q710F5E")

print(random.randrange(1,10))

#we can use """ while giving value to variable """
x = """likith avanthi csc-c"""
print(x)

#charecter positioning
x = "python"
print(x[1])

#looping through a string
#for loop in python
for x in "python":
  print(x)

#few examples in for loop in python
for y in "likith":
  print(y)

#string lenght 
a = "artificial intelligence"
print(len(a))

#example
b = "meruvu likith"
print(len(b))

#check string
x = "likith is very bad boy"      #for true onces
print("bad"in x)

#example
x = "likith is a good boy"        #for false onces
print("bad"in x)

#check string using if statements
x = "likith know python "
if "python"in x:                #for true
  print("yes","python is present")

x = "likith know AI"
if "python"in x:
  print("yes","AI is present")   #for false 

#checking true or false statements
x = "python is best"
print("AI" in x)

#true os false by if statements
x = "AI is best"
if "AI"in x:
  print("yes its there")

#slicing strings
x = "likith meruvu"  #letters of 0 and 6 position or :6 from starting 
print(x[:6])
print(x[7:])         #letters from 7 to end as 7:
print(x[-6:-2])       #reading string from back side
print(x[-13:])

#modify string
x = "likith"
print(x.upper())    #for upper cases
x = "AI"
print(x.lower())     #for lower cases
x = "likith is a good boy,he learns python program"
print(x.capitalize())   #for 1st letter capitalizing 

#strip string
x = "      likith"   #for removing space
print(x.strip())

#replacing string
x = "c language"
print(x.replace("c language","python"))    #replaces from left to right once

#split string
x = "hello,earth"
y = x.split(",")
print(type(y))
print(y)

#adding strings
x = "likith"
y = "meruvu"
z = x+y   #dont keep this as ("") if u kept ther will be printed x+y only not string
print(z)

#taking space between string addition
x = "likith"
y = "meruvu"
z = x+" "+y
print(z)

#string format
x = 18
y = "i am likith and iam {}"
print(y.format(x))

#example
rate = 500
quality = 1
quantity = 3
myorder = "i ordered {2} pieces of burger of rate {0} of type {1}"
print(myorder.format(rate,quality,quantity))

#example-2
x="liki"
y="meruvu"
z="likith"
myname = "my name is {2} my surname {1} my nick name {0}"
print(myname.format(x,y,z))

#python escape charecters
x="likith so called\"good boy\"is learning python"
print(x)

#single quote
x = "likith is \'good"
print(x)

#backslash
x = "likith\\\\(is good)"
print(x)

#new line 
x = "likith \nmeruvu"
print(x)

#carriage return
x = "likith \r meruvu"
print(x)

#\t for tab space  
#\b for back space
#\f for form feed

#octal value 
x = "\157\127\122\112\110"
print(x)

#hexadecimal
x = "\x69\x45\x65\x5f\x65"
print(x)

#centering 
x = "likith meruvu"
print(x.center(150))

#one program for course development
a = 300
b = 780
c = 325
d = 890
total = (a+b+c+d)
print(total/130)

#namespace and scope
liki = 100
def calculate():
  likith = 200
  sum = liki + likith
  total = sum
  print(total)
calculate();

#example with logic
liki = 100
def calculate():
  liki = 200
  likith = 205
  sum = liki + likith
  total = sum
  print(total)
calculate();
print(liki)

#using global variable 
liki = 100
def calculate():
  global liki
  liki = liki + 30
  likith = 200
  sum = liki + likith
  total = sum
  print(total)
calculate();
print(liki)





"""inter = int(input("enter your inter marks"))
btech = int(input("enter your  btech marks"))

job = (inter-btech)

print("my inter marks {},my b.tech marks {}, my job is {}".format(float(inter),float(btech),job))"""

a = 5
b = 2
a+=5
print(a)   # a value = 5

a-=5
print(a)  # 10

a/=b     #5
print(a)

a//=b     #2.5
print(a)

a%=b     #1.0
print(a)

a**=3    #1.0
print(a)


#age calculation program

"""yearofbirth = int(input("enter your birthyear"))
currentyear = date.today().day
age = currentyear - yearofbirth

print("your age is :",age)"""

name = "likith meruvu"
print(len(name))    #string lenght
print(name[1:12])
print(name[1:12:2])   #[start:end:step]
print(name[::-1])    #slicing string

#string concatination
channel = "kartx legend yt  " * 3     #multiply string 
channelnote = "kartx legend yt " + "subscribe "   #add string
print(channel)
print(channelnote)

#using in and not in statements

#in
print( "subscribe" in channelnote)
print("1k" in channelnote)

#not in
print("1k" not in channelnote)
print("subscribe" not in channelnote)

#lists

marks = [20,30,40,50,60,50]
print(len(marks))       # allows duplicate also in lists
print(marks[2]-marks[4])

#nested lists multidimentional lists
but = ["school","clg","b.tech","money"]
show = ["tired","of",but]
print(show)



#accessing elements in lists 

print(show[-1][-2])
#show[2][3]

#changing values in lists'

show[1] = "collage"
print(show*3)

#using appened and extend and insert
but.append("frds")
but.extend(["python","dsa","cse"])
print(but)

but.insert(0,"bhashyam")
print(but)

#using del command

name = [1,2,3,4,5,6,7,8,9,10]
del name[2:5]
print(name)

#using remove 
#pop
#push 

name.remove(1)
print(name)

print(name.pop(0))
print(name.pop())
print(name)

#tuples
mark = ('9','7','6','4')
#tuples  are immutable
#but  we can change values in tuple when list is there in tuple

sub = "phy","chem",["mathx","pps"]

print(sub[2])

name = { "likith","meruvu", "rohit","raju","ramu","somu","ajay"}
name.add("liki")
print(name)
name.update(["kartx","legend"])
print(name)

name.remove("liki")
print(name.pop())

#union 

a = {10,20,30,70,50}
b = {60,70,30,90,100}

abunion = a.union(b)     #or a|b also 
print(abunion)

#intersection
abintersection = a.intersection(b)    # a & b
print(abintersection)

#difference
abdifference = a.difference(b)   # a - b
print(abdifference)

#symmetric_difference
sydifference = a.symmetric_difference(b)   # a ^ b
print(sydifference)


#control flow

#if statments

"""n = int(input("enter you age"))

if (n >= 18):
  print("you can drive ")

elif (n == 12):
  print("wait 6 years ")

else:
  print("you cant drive")

#using nested if statments

n = int(input("enter any number "))

if n % 2 == 0 :
  if n % 4 ==0:
    print("congrats ")
  else :
    print("sorry ")
else:
  print("wt is this number ")"""

#program for b.tech admissions

"""rank = int(input("enter your eamcet rank --> "))

if rank in range(1,1001):  
  print("you will get admission in gitam collage ")
elif rank in range(1000,10001):  # rank > 1000 and rank <= 10000
  print("you will get admission in raghu  ")
elif rank in range(10000,40001):
  print(" you will get admission in avanthi ")
else :
  print("sorry you cant study b.tech")"""

#short hand if else statments

n = 6
print("its 6 good shot dhoni ") if n == 6 else print("no problem try next time ")

#iteration loops in python  

#for loops  used for fixed number of iteration

numberlist = [1,2,3,4,5,6,7,8,9,10]    #using integer

for number in numberlist:   #here numberlist is passing its values to number and printing them as user requirement
  print(number + 3 )

names = "likith meruvu"    # using string format for for looping system
for name in names:
  print(name)

#using range in for loops

for i in range(0,10,2):     # range(START,END,STEP)
  print(i)

#program for print 100 to 1 numbers 

for i in range(100,0,-1):
  print("the number is ",i)

#progrAM for print string last charecter and print 10 times

"""n = input("enter your name -> ")
name = n[-2:]

for i in range(1,11):
  print(" ",name)"""

#iterations in lists , tuples , dictionaries

#lists

a = ["likith","rohit","karthik","sankar"]

for element in a:     #elements passes the index of list elements
  print(element)

#tuples

b = ("liki","hello","world")

for i in b:     #same as lists
  print(b)

c = {1:"liiki",2:"likith",3:"rohit"}

for i in c:    #in here the dictionary element number will be inserted in i and called using c[i]
  print(i)
  print(c[i])


# program for vowels and consonents

"""n = input("enter your name --> ")

vowels = ["a","e","i","o","u"]

for elements in n:       # giving n to the elements 
  if elements in vowels:   # if elements are there in vowels 
    print(elements,"- is vowel ")

  else:
    print(elements,"- is a consonent")"""

#loops control statements 
#break  #continue  #pass

# break (used to break the loop in the middile)

n = {1:"likith",2:"print",3:"input"}

for i in n:
  print(i,"is the number")
  break

# continue statements (used to point loop to starting )

h = {1:"likith",2:"print",3:"input"}

for i in h:
  print(i)
  continue
print("hehe boi")

# pass statments (place holder )

l = {1:"likith",2:"print",3:"input"}

for i in l:
  pass  # place holder for furthur use or change in the program 

# program to add sum of marks sum using for loops

marks = [10,30,50,60,70,100]
sum = 0
for i in marks:
  sum = sum + i

print("total sum is -",sum)


#while loops (used when there is no idea how amny loop should be exicuted for the user requirement )

''' syntax --- while (expression)
            -------code -------
'''
  
#program for while loop basic 
n = int (input("enter any number below 100 "))
while n<=100:
  n = n + 1
  print(n)


#[functions in python ] (main topic in python)

print("___________function_____________")

'''' syntax -     def function name (parameters):
                ---- code ------                 '''

def squareroot (number):
  n = number**2
  print("the number square root is ",n)

squareroot(5)

#other examples

def loop (n):
  n = 0
  l = int(input("enter your end range number for iteration --> "))
  for i in range(0,l + 1):
    n = n + i
    print(n)

k = int(input("enter your number for iteration --> "))
loop(k)

print("---------functions-----------")

#  program for add, sub , mul ,divide , modulus ,square
from functools import reduce

def add ():
    "used to add 2 integers"    #doc to get info of this funtion  #syntax = functionName.__doc__
    x = int(input("enter any number -->"))
    y = int(input("enter any number -->"))
    print(x + y)
     
def sub ():
    "used to substract 2 integers"
    X = int(input("enter any number -->"))
    Y = int(input("enter any number -->"))
    return(X - Y)     # can use return funtion also instead of print 

def mul ():
    "used to multiply 2 integers"
    a = int(input("enter any number -->"))
    b = int(input("enter any number -->"))
    print(a * b)

def div ():
    "used to divide"
    A = int(input("enter any number -->"))
    B = int(input("enter any number -->"))
    print( A / B)

def mod ():
    c = int(input("enter any number -->"))
    d = int(input("enter any number -->"))
    print( c % d)

def pow ():
    e = int(input("enter any number -->"))
    f = int(input("enter any number -->"))
    print( e ** f)



#reference in function

a = 10
marks = [10,20,30,40]

marks[2] = a      # changing the value reference in variable 
print(marks)

a = 10
marks = [10,20,30,40]

marks = a      # changing the refenrence of complete variable
print(marks)


# changing the va;ue reference in variable using functions

def varref (n):
    n[2] = 100
    return n

marks = [1,2,3,4,5,6]
print(varref(marks))


# changing the complete reference of the variable

def var (n):
    n = 10
    return n

marks = [1,2,3,4,5,67,67]
print(var(marks))     # completely ref changed variable with different memory allocated
print(marks)   # normal variable with diff memory allocation



# default arguments

def phone (x = 10000):
    print("your phone price is ",x)

print(phone(2000))
print(phone())


#key word arguments

def mobile (ram,rom,price,battery):
    print("the ram is ",ram, "the rom is ",rom, "the price of mobile is",price, "the battery capacity is",battery)

# redmi = mobile(8,128,20000,4500)
redmi = mobile(rom = '128',price = '20000',battery = '4500 mah',ram = '8')
print(redmi)

#variable number of arguments  (multipule arguments)

def value (*lol):     #giving multiple arguments with (*) symbol to the argument
    for i in lol:
        #i = i + 1
        print(i)

print(value(1,3,4,3,4,56,))  


def multiply (start,*args):
    mult = start
    for i in args:
        mult = mult + i
        print(mult)

op = multiply(10,2,4,6,8)
print(op)


#using yield keyword in functions

def burger (n):
    calories = n * 200
    yield calories     # statement 1  (yield is used to return and resume back and execute the forward code)
    print("y r u eating")   # statement 2 (forward code )

food = burger(3)
print(food)
for i in food:   # accessing the 1 and 2 statements in function using loops  
    print(i)

#lambda functions (anonymous functions)

cube = lambda num :num**3    #syntax --- variable =  lambda (variable) :expression in single line
print(cube(4))   


#using filter funtion  syntax --- filter(funtion,iteration or list)

def evenorodd (n):
    return n % 2 == 0

n = [10,34,56,77,99]
result = filter(evenorodd,n)
print(list(result))

#using anonymous funtion with filter
#(it filters the list with given user condition)
n = lambda num : num % 2 == 0
num = [12,33,45,60,54]
r = filter(n,num)
print(filter(n,num))
for i in r:
    print(i)

#using map
#same as filter syntax   ---- map(function,iteration)
k = ["likith","meruvu"]
n = map(lambda num : num.upper(),k)
print(n)
for i in n:
    print(i)

#using reduce 
#from functools import reduce
k = [10,20,34,56]
n = reduce(lambda a,b :a+b,k,10 )
print(n)
# here object is not created for reduce so there is no need of using for loop for output



print("=============------------    OOPS BASICS     ------------==========")

class jarvis():
    "just testing purpose of jarvis.py"
    creator = "likith meruvu"

    def __init__(self,gui,cli):
        self.gui = gui
        self.cli = cli
        print(gui)
        print(cli)

    def guifunction (self):
        print("opening jarvis graphical interface.....")

    def clifunction (self):
        print("opening some commands of jarvis...")

user = jarvis("gui tlinker","cli likith ")
print(user.creator)
print(jarvis.__doc__)

user.guifunction()
user.clifunction()


class alexa(jarvis):

    def __init__(self, gui, cli):    #creating a child class constructor
        super().__init__(gui, cli)     #super keyword used to call parent class constructor without calling self
        #jarvis.__init__(self,gui,cli)  we can call the parent class consturtor directly like this         
        
    
    def newassistant (self):
        print("welcome to alexa work assistant ")

user1 = alexa("hi","hello")
print(user1)
print(user1.creator)
user1.guifunction()
user1.clifunction()

print("==========------------------   types of inhertance in oops   --------------------========== ")

#types of inheritance

# 1. single inheritance
# 2. multiple ""
# 3. multilevel ""
# 4. hierarchical ""
# 5. hybrid "" (it consistes of multilevel ,hierarchi , and multiple inheritance)

#single is easy done in oops basics

# multiple inheritance(one child class accessing multiple parent class)
print("=================----------       multiple inheritance        ----------==========")
class classa ():
    def eat():
        print("eating")

class classb ():
    def drink():
        print("drinking")

class classc (classa,classb):
    def sleep ():
        print("sleeping good morning")

n = classc
n.eat()
n.sleep()
n.drink()

#multilevel inheritance(one child class is accessing the other parent class and parent class is acessing the other class)
print("================---------      multilevel inheritance-------================")
class class_a ():
    def eat():
        print("eating")

class class_b (class_a):
    def drink():
        print("drinking")

class class_c (class_b):
    def sleep ():
        print("sleeping good morning")

n = classc
n.drink()
n.eat()


#hierarchial inheritance (all child classes are accessing one parent class )

print("======---   -----          hierarchi inheritance   -----=========== ")

class class_a ():
    def eat():
        print("eating")

class class_b (class_a):
    def drink():
        print("drinking")

class class_c (class_a):
    def sleep ():
        print("sleeping good morning")

n = class_c
l = class_b
n.eat()
l.eat()



print("==============---------         encapsulation         --------===============")

print("access Modifiers")

#encapusulation accessing modes

#protected mode
class food():
    owner = "likith"
    def __init__(self,snacks,drinks):
        self.__snacks = snacks    #__means private
        self._drinks = drinks     #_means protected
        print(snacks)
        print(drinks)

    def eat():
        print("eating")

class test(food):
    def testing(self):
        print("test")

l = test("chips","spirite")


#polymorphism  (many forms)

#method overloading
"we cant create a two same functions in a class with same function name but we can pass multiple arguments through the functions using *args  and **args for keyword arguments"

#method overwritting
"child class function with same name function in parent class but if we call  the child class method will override the parent class method"

#exception handling in python 
# syntax error (stops the program in middle and throws error)
# exception error (runs the program to end and throw error in middle of program execution)

"there are lots of exception error in python"

import sys 

try:
    marks = ("likith", "li","lik")
    print(marks[0])

except SyntaxError:
    n = sys.exc_info()
    print("syntax wrong",n)
 
except IOError:
    i = sys.exc_info()
    print("index error",i)
except:     #none of the top error then it executes this block
    print(sys.exc_info())

else:     # we can use except or else if there is no error
    print("no error")

finally:
    print("i can executed even there is error or no error ")

#file handling in python

print("==========----------         file handling in python          ---------==========")

# access modes of file handling

# read only - (r)
# write only - (w)
# read and write - (r+)
#  write and read - (w+)
#  append only - (a)
#  append and read - (a+)
import sys

f = open('likith.txt', 'r')    # reading the created file 
file = f.read() 
print(file)
f.close()

f = open('likith.txt','r+')
file = f.read()       # read and write in file 
file = f.write("hello guys welcome to kartx legend yt ")         
print(file)
f.close()

f = open('likith.txt','a')   # using append function for writing and cursor will placed at end of the file
file = f.write("hello poor fellow")  # and it creates the new file of there is no file 
f.close()

with open('likith.txt','w') as file:    #using with can replace variable declaration like this variable file (object)
  file.write("thx for nothing")   # no need to close the file with will do automatically for us 
