#Argument functons
'''
def func_01(lname):
    print("Hello", lname)

func_01("Mohan") '''  


#Multiple Argument
'''
def func_01(fname,lname):
    print("Hello",fname,lname)

func_01("Mohan","Raj")    
'''


#keyword Argument
'''
def func_01(fname,lname):
    print("Hello",fname,lname)

func_01(lname="Raj",fname="Mohan")'''


#Arbitary keyword
'''
def func_01(* tname):
    print("Hello",tname[2])

func_01("apple","banana","cherry")

'''
#Arbitary keyword Arguments
'''
def func_01(**greet):
    print("Hello",greet["key2"])

func_01(key1="mango",key2="orange") '''


#default parameter value
'''
def func_01(tname="dove"):
    print(tname)
    
func_01("hen")
func_01("duck")
func_01()'''


#Return keyword
'''
def func_ret(x):
    return x**x
    
print(func_ret(5))
'''

#Basic function
'''
def my_func(a):
    print("The sum is",a)
    
my_func(5)  
'''

#lambda functions
'''
multi=lambda a,b : a+b
print(multi(5,10))


multi=lambda a,b : a+b
print(multi("mohan","raj"))
'''


#lambda function
'''
def fun(x,y):
      return lambda z:z+x+y
lamb=fun(5,10)
print(lamb(15))'''

'''
def fun(x,y):
    return lambda z:z*x*y
lamb=fun(10,20)
print(lamb(30))'''


#Arbitary keyword lambda function
'''
def fun(**kids):
    return lambda z:z+kids["x"]+kids["y"]
lamb=fun(x=10,y=20)
print(lamb(10))'''

'''
def fun(**kids):
    return lambda z:z*kids["x"]*kids["y"]
lamb=fun(x=20,y=20)
print(lamb(30))'''


#Print Reverse number
'''
x=int(input("Enter the Input: "))

temp=x
y=0

while(temp>0):
    n=temp%10
    y=(y*10)+n
    temp=temp//10
print(y)
'''

#Amstrong Number
'''
num=int(input("Enter the Number: "))
n=len(str(num))

temp=num
sum=0

while(temp>0):
    digit=temp%10
    sum=sum+(digit**n)
    temp=temp//10
if(num==sum):
    print(num,"Is a Amstrong Number")
else:
    print(num,"is not Amstrong Number")
    '''
    
    
#Amstrong Number Task
'''
num1=int(input("Enter the Number1: "))
num2=int(input("Enter the Number2: "))
n=len(str(num1,num2))

temp1=num1
temp2=num2
'''
'''
#write a program to compute the sum of the first 5 natural numbers
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
        
    
#tup1=[get values from user]
#tup2=[get values from the user ]
#Multiply the values on the basis of index number and print result in set

tup1=int(input("Enter the value tup1: "))
tup2=int(input("Enter the value tup2: "))

for i in range(1,11):
    print(i)
'''
'''
def outer_fun():
    print("Hello Brother")
    def inner_fun():
        print("shall we")
    inner_fun()
outer_fun()
'''
'''
def fun(num):
    a,b=0,1
    while 0<num:
        yield a
        a,b=b,a+b
obj=fun(10)
for i in obj:
    print(i)
'''
'''
def display(*a):
    print("Arbitrary arguments")
    print(a)
display("Hello","Mohan","How are you")    
'''

#Decorators
'''
def UpperString(ref):
    def process():
        data=ref()
        return data.upper()
    return process
@UpperString
def MyFunc():
    return 'welcome to python'
    
MyFunc()
'''
#Decorators
def OuterFunction(ref):
    def InnerFunction(*args):
        return ref(*args).upper()
    return InnerFunction
@OuterFunction
def MyFunction(str1,str2):
    return f'hello {str1} and {str2}'
print(MyFunction('ram','sam'))

#obj=OuterFunction(MyFunction)
#print(obj('ram','sam'))
    






