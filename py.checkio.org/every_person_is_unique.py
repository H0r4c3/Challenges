'https://py.checkio.org/en/mission/every-person-is-unique/'

'''
You have to create a class ‘Person’ and a few methods to work with its instances. See the class description below.

class Person (first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')

It returns a new instance of the ‘Person’ class with the name and surname [ first_name , last_name ], date of birth - birth_date (in 'dd.mm.yyyy' format), 
current job - job , number of working years - working_years , average salary - salary (per month), current country and 
city - [ country , city ] and gender - gender . 
The gender parameter could be 'male' or 'female'. If this parameter is undefined, the default value is - 'unknown'.
'''

from datetime import datetime, date

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender
        
    def name(self):
        '''Returns the full name (name and surname, separated by a whitespace)'''
        return f'{self.first_name} {self.last_name}'
    
    def age(self):
        '''Returns the person’s age - the number of fully lived years. (The current date is 01.01.2018)'''
        format_data = "%d.%m.%Y"
        date1 = datetime.strptime(self.birth_date, format_data)
        date2 = datetime.strptime('1.1.2018', format_data)
        return int((date2 - date1).days // 365.2425)
    
    def work(self):
        '''Returns the person’s job in a sentence as follows: ‘He is a ...’ (if male) ‘She is a ...’ (if female) ‘Is a ...’ (if unknown)'''
        if self.gender == 'male':
            return f'He is a {self.job}'
        elif self.gender == 'female':
            return f'She is a {self.job}'
        else:
            return f'Is a {self.job}'
    
    def money(self):
        '''Returns an amount of money, earned during the working years. 
        It should be returned in format xx xxx … - every 3 decimal places should be separated by a whitespace. 
        For example: ‘10 568’ ‘1 051 422’'''
        amount_of_money = self.working_years * 12 * self.salary
        return f'{amount_of_money:,}'.replace(',', ' ')
    
    def home(self):
        '''Returns the country and the city where a person lives: ‘Lives in the city, country’'''
        return f'Lives in {self.city}, {self.country}'
    
      
p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")   
print(p1.name())
print(p1.age())
print(p1.work())
print(p1.money())
print(p1.home())
        
    


# Best Solution: 
# https://py.checkio.org/mission/every-person-is-unique/publications/dobyvillanueva/python-3/first/share/b53299f664bd6de1b92c8a180c5ca278/

from datetime import date
class Person_:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
        
    def age(self):
        dd, mm, yyyy = map(int, self.birth_date.split('.'))
        return int((date(2018,1,1) - date(yyyy,mm,dd)).days/365.2425) # should have been date.today() but "today" date is specified as 2018,1,1

    def work(self):
        if self.gender is "male":
            prefix = "He is"
        elif self.gender is "female":
            prefix = "She is"
        else:
            prefix = "Is"
        return "{start} a {work}".format(start=prefix, work=self.job)
        
    def money(self):
        return "{:,}".format(self.working_years * 12 * self.salary).replace(',', ' ')
        
    def home(self):
        return "Lives in {city}, {country}".format(city=self.city, country=self.country)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")