1.Dictionaries
given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension

nums = [1, 2, 3]
SqrDict = {x:x**2 for x in nums}
SqrList=[x for x in SqrDict.values()]
print(SqrDict)
print(SqrList)


2.
set comprehension
given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}

NumList = [1, 2, 5, 2, 3, 1, 4, 5]
SqrSet = {x**2 for x in set(NumList)}
print(SqrSet)


3. Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:

3.1 dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}

tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
dict= {x:y for (x,y,z) in tuplist if y>=z}
print(dict)


3.2 set of all balances {2000, -52, 900}

tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
s=set( [y for (x,y,z) in tuplist])
print(s)


3.3 list of account holders ["Guido", "Raymond", "Jack", "Brandon"]

tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
accList= [x for (x,y,z) in tuplist]
print(accList)


3.4 
dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}

tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
dict= {x:abs((y-z)) for (x,y,z) in tuplist if y<z}
print(dict)

3.5
list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]
tuplist = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
AccList= [x for t in tuplist if t[1]> 0 for x in t[0:2]]
print(AccList)






4. Write a Developer class that has a code function and a languages list.

code function should accept a language param and if the language is in the languages list it should print code in <language>.
resume function that prints languages of the developer.
Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.
Write a TechLead class that inherits from SrDeveloper and adds design function

class Developer:
 def __init__(self):
    self.langList= []
 def code(self,plang):
    if plang not in self.langList:
     self.langList.append(plang)
    else:
     print(plang) 
 def resume(self):
  print( "List", self.langList)

class SrDeveloper(Developer):
  def __init__(self):
    Developer.__init__(self)
  def review(self,lang1):
    self.langList.append(lang1)
    print("Review list", self.langList)
class TechLead(SrDeveloper):
  def __init__(self):
    SrDeveloper.__init__(self)
  def design(self,lang1):
    self.langList.append(lang1)
    print("Design list", self.langList)
o1 = Developer()
o1.code("Python")
o1.code("PLSQL")
o1.code("PLSQL")
o1.resume()
o2= SrDeveloper()
o2.review("Java")
o3= TechLead()
o3.design("DONT KNOW WHAT TO DO")




5. create a class that provides the factorials for the list of numbers provided.
import math
class Factclass:
 langList= []
 def __init__(self,num):
   self.num=num
 def fact(self):
   print(math.factorial(self.num))
   #print(self.num)

o1 = Factclass(5)
o1.fact()

------
6. 
 def square(num):
  print( num**2)
  
  
  import mymodule
  square(5)

could not import .
I needed guidance where to save file as I use repl.it to execute code
tried command prompt as well but did not work.



7. import a func and rename it to use in your module from another
   import math as factmath
   class Factclass:
	langList= []
	def __init__(self,num):
	  self.num=num
	   #Developer.langList=["English","Hindi"]
	def fact(self):
	   # return self.math.
	  print(factmath.factorial(self.num))
	   #print(self.num)

	o1 = Factclass(5)
	o1.fact()

8. create a module that prints "I'm running" only when it's ran as a script (not as a module using import)
- did not understand what to do 
9. use python to open another python source file and print the contents
-could not do it