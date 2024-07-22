class Employee():
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(' ')[0]
        self.lname=value.split(' ')[1]

x=Employee()
x.name="ayush garkoti"
print(x.lname,x.fname)

# encapsulation mttlb humne bhaut sare kaam krne wali chizon ko ek class mai wrap  kr dia
# abstraction mtlb humne kya chl raha hai background mai usey user se hide kr dia