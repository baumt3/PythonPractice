# Importing the Person class for inheritance
import person

class Customer(person.Person):
    def __init__(self, name, address, telephone, customer_id, is_on_mailing_list):
        # Call the constructor of the parent class (Person) to initialize common attributes.
        super().__init__(name, address, telephone)
        
        # Additional attributes specific to the Customer class.
        self.__customer_id = customer_id
        self.__is_on_mailing_list = is_on_mailing_list
        
    def set_customer_id(self, customer_id):
        # Setter method to update the customer's ID.
        self.__customer_id = customer_id
        
    def get_customer_id(self):
        # Getter method to retrieve the customer's ID.
        return self.__customer_id
        
    def set_is_on_mailing_list(self, is_on_mailing_list):
        # Setter method to update whether the customer is on the mailing list.
        self.__is_on_mailing_list = is_on_mailing_list
        
    def get_is_on_mailing_list(self):
        # Getter method to retrieve whether the customer is on the mailing list.
        return self.__is_on_mailing_list

