class Employee:
    #pass
    
    #class variables [same as global variables in Java]
    pay_raise_amount = 1.05 #increasing payment by 5%
    
    # init method = constructor/initialize
    def __init__(self, first, last, phone, pay):
        self.first = first
        self.last = last
        self.name = first + " " + last
        self.pay = pay
        self.phone = phone
        self.email = first.lower() + last.lower() + "@loblaw.com"
        
    def apply_raise(self):
        #print(f"Request: Please raise the monthly salary of {self.name}.")
        if self.pay<50000:
            self.pay += 5000
            print(f"Raise approved. Increasing salary for {self.name}.")
        else:
            print("No raise applicable for", self.name, ".")
            
    def apply_raise_pct(self):
        self.pay = int(self.pay * self.pay_raise_amount) 
        
emp1 = Employee("Sama", "Samrin", 3580745, 50000)
emp2 = Employee("Sabab", "Salam", 1716034, 45000)
emp3 = Employee("Samira", "Saba", 1715478, 40000)

# raise the salary of eligible employees 
emp2.apply_raise()
print (f"{emp2.name} earns {emp2.pay} taka now.\n")
emp1.apply_raise()
print (f"{emp1.name} earns {emp1.pay} taka now.\n")
emp3.apply_raise()
print(f"{emp3.name} earns {emp3.pay} taka now.\n")

emp2.apply_raise_pct()
print (f"{emp2.name} earns {emp2.pay} taka after new raise.\n")
emp1.apply_raise_pct()
print (f"{emp1.name} earns {emp1.pay} taka after new raise.\n")
emp3.apply_raise_pct()
print(f"{emp3.name} earns {emp3.pay} taka after new raise.\n")
