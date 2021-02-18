1 Create a class that implements __iter__ and __next__ methods.

class ItrDemo:
 def __init__(self):
  self.inp=[]
 def Itr(self,InputString):
  print(InputString)
  self.inp= InputString
  it=iter(self.inp)
  try:
   for x in range(len(InputString)):
     #print(next(it))
     #print(InputString[x])
     print(next(it))
     next(it)
  except StopIteration:
    pass
  finally:
   print("Iteration is done")
o1 = ItrDemo()
o1.Itr("Hello")


2. create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.
	f = open("Myfile_as.txt", "a")
	dictname = {"Joy":2,"Meeta":4,"Savio":5}
	for x,y in dictname.items():
	 # print(f"{x} , {y}")
	  wvalue= x + ',' + str(y)
	  print(wvalue)
	  f.write(wvalue)
	  f.write("\n")
	f.close()
	
3. write a program to traverse the current directory (recursively) and print only python file names.
import glob
home = 'C:\Users\807324\Desktop\PY'
for filename in glob.iglob(home + '**\*.py', recursive=True):
    print('filenames are ', filename)
	
4. use standard lib sys to list all the command line args given to your program
  ---- not able to run it in repl
 if __name__ == "__main__":
    print(f"Arguments Number: {len(sys.argv)}")
    for i, argument in enumerate(sys.argv):
        print(f"Argument {i:>6}: {argument}"

5. Rewrite the guessing game program to throw a custom error when the user is out of tries.

for t in range(4):
  try:
   if t==3:
    raise Exception("out")
   a=int(input("Enter a Number: "))
   h_num=10
    #print(a)
   if a>h_num:
     print(str(a) +" is greater than 10")
   elif a == h_num:
     print(str(a) +" is equal to 10")
   else:
     print(str(a) +" is less than 10")
  except:
    print("Sorry, This is it, no more try")
    
   
6. accept input from a user and handle type, value errors
import math
try:
 y= int(input("Enter a Value - ") )
 print(y)
 z= math.factorial(y)
 print(f"factorial of {y} is {z}")
 x= input("Enter a Value - ")  
 x+10
 print(x)
except TypeError:
    print("Type error Demo")
except ValueError:
  print("Value error demo")
finally
  print("we are done")
  
7. demonstrate key and index errors in an example
Key Demo


Index Demo-
try:
 NewList=["Joy","Savio","Max"]
 for x in range(4):
  NewList[x]="Hello "+NewList[x]
  print(NewList[x])
 else:
  print(NewList )
except IndexError:
    print("Index Error Demo")
finally:
 print("We are done")

 
 Key error-
 
 try:
  dictname = {1:"Joy",2:"Meeta",3:"Savio"}
  #newlist = [x for x in dictname.keys() if len(x) > 4]
  newdict = {k:v for (k,v) in dictname.items()if k>1}
  print(newdict)
  print(newdict[2])
  print(newdict[1])
except KeyError:
  print("Key error Demo")
except:
  print("other exception")
finally:
  print("we are done")