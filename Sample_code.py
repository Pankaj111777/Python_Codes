class Employee:
    company = "Persistent"
    
    def getSalary(self, signature):
        print(f"Salary for this employee Working in {self.company} is {self.salary}\n {signature}")
        
        

    def greet(self):
        print("Good Morning, Sir")
        
harry = Employee()
harry.salary = 1000000
harry.getSalary("Thanks!") 
harry.greet()       