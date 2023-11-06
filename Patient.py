# Create a class called Patient
class Patient:
    # The __init__ method will initialize the full name, address, phone number, and emergency contact attributes
    def __init__(self, full_name, address, phone_number, emergency_contact):
        # Create the instance variables that will store the information provided by the user.
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact = emergency_contact

    # Use the accessor methods to retrieve the attribute values.
    def get_full_name(self):
        return self.full_name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact(self):
        return self.emergency_contact

    # Use the mutactor methods to change the attributes if needed
    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_emergency_contact(self, emergency_contact):
        self.emergency_contact = emergency_contact

    # Display the informtaion
    def display_info(self):
        print("Patient Information:")
        print("Full Name:", self.full_name)
        print("Address:", self.address)
        print("Phone Number:", self.phone_number)
        print("Emergency Contact:", self.emergency_contact)
        print()