# Create the Employee class
class Employee:
    def __init__(self, name, employee_id):
        # The constructor initializes an Employee object with a name and id.
        # Using double underscores to make these attributes private.
        self.__name = name
        self.__employee_id = employee_id
        
    # Setter method to update the employee's name.
    def set_name(self, name):
        self.__name = name
        
    # Setter method to update the employee's id.
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id  # Fix: Use self.__employee_id instead of self.employee_id
        
    # Getter method to retrieve the employee's name.
    def get_name(self):
        return self.__name
    
    # Getter method to retrieve the employee's id.
    def get_employee_id(self):
        return self.__employee_id