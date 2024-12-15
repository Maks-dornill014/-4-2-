class Person:
    def __init__(self, name):
       
        self.name = name

    def age(self, birth_year, current_year):
        
        return current_year - birth_year


class Driver(Person):
    def __init__(self, name, driver_license_number):
        
        super().__init__(name)
        self.driver_license_number = driver_license_number

    def driver_info(self):
    
        return f"Водій: {self.name}, Номер посвідчення: {self.driver_license_number}"



person = Person("Іван")
print(f"Особа: {person.name}, Вік: {person.age(1990, 2024)} років.")

driver = Driver("Олександр", "AB123456")
print(driver.driver_info())
print(f"Вік водія: {driver.age(1985, 2024)} років.")
