# Importing the Employee class for inheritance
import employee

class production_worker(employee.Employee):
    def __init__(self,name, employee_id, shift, hourly_pay_rate):
        # Call the constructor of the parent class (Employee) to initialize common attributes.
        super().__init__(name, employee_id,)
    
        # Additional attributes specific to the production_worker class. 
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate
    
    def set_shift(self, shift):
        # Setter method to update the shift.
        self.__shift = shift
    
    def get_shift(self):
        # Getter method to retrieve the shift. 
        return self.__shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        # Setter method to upate the hourly_pay_rate
        self.__hourly_pay_rate = hourly_pay_rate
    
    def get_hourly_pay_rate(self, hourly_pay_rate):
        #Getter method to retrieve the hourly_pay_rate
        return self.__hourly_pay_rate