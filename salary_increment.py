"""class Employee():
    name = input("enter name: ")
    salary=int(input("enter salary: "))
    company="google"
    years_worked=int(input("enter years worked: "))
    if years_worked <= 1:
        increment = 0
    elif 1 < years_worked <= 5:
        increment = 20
    else:
        increment = 50
    def __init__(self, ename , company , salary , years_worked):
        self.ename=ename
        self.company=company
        self.salary=salary
        self.years_worked=years_worked
        def increment(self):
        if self.years_worked<=1:
            print("sorry you are not eligible for increment!")
        elif 1<self.years_worked<=3:
            self.salary=self.salary+(self.salary*0.25)
        else:
            self.salary=self.salary+(self.salary*0.40)
        print("salary after increment is :",self.salary)
x=Employee('ayush',"google", 2500000,3)
x.increment()
x=Employee('ayush',"google", 4375000.0,5)
x.increment()
    @property
    def increase(self):
        return (self.salary+(self.salary*self.increment/100))
    @increment.setter
    def increment(self,salary):
        return ((salary/self.salary)-1)*100

e=Employee()
print(e.increase)"""


class Employee:
    def __init__(self):
        self.name = input("Enter name: ")
        self.salary = int(input("Enter salary: "))
        self.company = "Google"
        self.years_worked = int(input("Enter years worked: "))

        if self.years_worked <= 1:
            self._increment = 0
        elif 1 < self.years_worked <= 5:
            self._increment = 20
        else:
            self._increment = 50

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = value

    @property
    def increase(self):
        return self.salary + (self.salary * self.increment / 100)


# Create an instance of Employee
e = Employee()
print(e.increase)






