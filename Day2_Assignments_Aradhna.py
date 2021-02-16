# 1.Improvise the guessing game from yesterday by providing 3 tries to the player
for t in range(3):
 a=int(input("Enter a Number: "))
 h_num=10
 #print(a)
 if a>h_num:
   print(str(a) +" is greater than 10")
 elif a == h_num:
   print(str(a) +" is equal to 10")
 else:
   print(str(a) +" is less than 10")
   
 
 #2.Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
 
  name=['A','B','C','D','E','F']
  for ind,name in enumerate(name):
   print(ind ,':',name)
 
 #3.Loop over a dict and print the value and key in the format value belongs to key.
stu_dict={"name":"Joe","age":20,"place":"Mumbai"}
for dict in stu_dict:
  print(f"{dict} => {stu_dict[dict]}")
  
#4.Demonstrate the else clause being invoked in a while loop. try the opposite as well.
 a=0
 while a < 5:
 print(a)
 a+=1 
 else:
  print("While demo finished")
  
#5.write an add function that accepts two numbers and returns their sum
use type hints
use docstring

def funcDemo(a,b):
  """This is a function Demo"""
  print(f"a => {type(a)}",f"b => {type(b)}")
  return a + b
print(funcDemo.__doc__)
print(funcDemo(a=10,b=20))


#6. write a function that accepts any number of args and prints them to the screen one per line

def argDemo(*args):
 for n in args:
   print(f"Hello there {n}")
 
print ("one argument")
argDemo("Joe")
print ("two argument")
argDemo("Joe","Monica")
print ("three argument")
argDemo("Joe","Monica","Ross")

#7.write a function that accepts any number of kwargs and prints the number of orgs

def argDemo(**kargs):
 for n in kargs:
   print(f" {n} : {kargs[n]}")
 
print ("one key argument")
argDemo(Name="Joe")
print ("two key argument")
argDemo(Name="Joe",city="Mumbai")
print ("three key argument")
argDemo(Name="Joe",city="Mumbai",age = 20)

#8.write a function that accepts any number of args and/or kwargs and prints the count of both

def argDemo(**args):
   print(len(args))
print ("one key argument")
argDemo(Name="Joe")
print ("two key argument")
argDemo(Name="Joe",city="Mumbai")
print ("three key argument")
argDemo(Name="Joe",city="Mumbai",age = 20)

9.Go through PEP 8, and try refactoring your code

10.Go through PEP 20 and let me know your fav one!
Simple is better than complex

#11.Do a while loop with and without else block getting invoked
 a=0
 while a < 5:
 print(a)
 a+=1 
 else:
  print("While demo finished")
  
 #without else
 a=0
 while a < 5:
 print(a)
 a+=1 

 #12 Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
 
 num = [1, 3, 3, 4, 5, 6]
 #1 3 3 5
 newlist = [x**2 for x in num if (x%2)>0]
 print(newlist)
 
 #13 write a lambda expression to return average given a total and count
x = lambda a,b : a /b
num=int(input("Enter a Number- "))
cnt=int(input("Enter a Count- "))
print(x(num,cnt))

Bonus
1. Try list comp to get keys that are longer than 4 chars in a dict

dictname = {"firstname":"Joy", "city":"Mumbai","profession":"Salesman", "Birthyear":1990}
newlist = [x for x in dictname.keys() if len(x) > 4]
print(newlist)


2. Try list comp to get keys that are longer than 4 chars in a dict
implement nested list comp in any use case
StudentDict = {
  "Student1" : {
    "FirstName" : "Aradhna",
    "LastName" : "Sharma",
    "Grade" : 5
  },
  "Student2" : {
   "FirstName" : "Bhavana",
    "LastName" : "Sahu",
    "Grade" : 10
  },
  "Student3" : {
   "FirstName" : "Preksha",
    "LastName" : "Tiwari",
    "Grade" : 8
  }
}
for dict in StudentDict:
  print(f"{dict} => {StudentDict[dict]}")
