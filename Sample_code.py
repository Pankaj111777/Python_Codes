class Employee:
    company = "Persistent System"
    
    def getSalary(self, signature):
        print(f"Salary for this employee Working in {self.company} is {self.salary}\n {signature}")
        
        

    def greet(self):
        print("Good Morning, Prajwal Sir")
        
harry = Employee()
harry.salary = 2586322
harry.getSalary("Thanks so much !") 
harry.greet()       
