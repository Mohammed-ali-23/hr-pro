
class Employee:
    def __init__(self,name, age, salary, employemnt_years):
      self.name = name
      self.age = age
      self.salary = salary
      self.employemnt_years = employemnt_years
    
    def get_annual_salary(self):
        return self.salary * 12








   #Employee class here

class Manager(Employee):
    def __init__(self,name, age, salary, employment_years, bonus_percentage):
      self.name = name
      self.age = age 
      self.salary = salary
      self.employment_years = employment_years
      self.bonus_percentage = bonus_percentage

    def bonus_percentage(self):

         return(self.bonus_percentage * self.salary)
    def __str__(self.manager) -> str:
        return super().__str__()
        
        
       Employee = []

         

        




    #Manager class here
        
def main():
	# main code here

if __name__ == '__main__':
	main()
