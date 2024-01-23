class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
      
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
   
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
     
    def __repr__(self):
        return "Employee('{} {} {}')" .format(self.first, self.last, self.pay)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Name Deleted!')
        
class Manager(Employee):
    def __init__(self, first, last, pay, Employees = None):
        super().__init__(first, last, pay)
        pass

emp1 = Employee('Len','Kim', 100000)
emp1.fullname = 'John Doe'


print(emp1.first)
print(emp1.pay)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)


    