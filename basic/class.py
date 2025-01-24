# class X:
#     def add(self,x,y):
#         addi=x+y
#         print(addi)
        
#     def subs(self,m,n):
#         sub=m-n
#         print(sub)
        
# class Y(X):
#     def multi(self,m,n):
#         mul=m*n
#         print(mul)
        
# class Z(Y):
#     def div(self,x,y):
#         divv=x/y
#         print(f"The ans of x / y is {divv}")
        
class exp:
    def myname(self,name):
        nam=name
        print(f"My name is{nam}")
        
class clas(exp):
    def section(self,secti):
      sectio=secti
      print(f"Division is {sectio}")
    
class rol(exp):
    def rol_no(self,rolll):
        roll_no=rolll
        print(f"My rollno is {roll_no}")
        
        
# obj=Z()
# obj.multi(5,2)
# obj.add(1,2)
# obj.div(10,2)

obj=clas()
obj.section('4A10')
obj.myname('AAyush')


obj1=rol()
obj1.rol_no(13)
obj.myname('Aayush')






# class Student:
#     _name = None
#     _roll = None
#     _branch = None

#     def __init__(self,name,roll,branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
        
#     def _displayRollAndBranch(self):
#         print("Roll:",self._roll)
#         print("Branch:",self._br
    
        
        