class Patient:
    def __init__(self, full_name, address, phone_number, emergency_contact):
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact = emergency_contact

    def get_full_name(self):
        return self.full_name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number

    def get_emergency_contact(self):
        return self.emergency_contact

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_emergency_contact(self, emergency_contact):
        self.emergency_contact = emergency_contact

    def display_info(self):
        print("Patient Information:")
        print("Full Name:", self.full_name)
        print("Address:", self.address)
        print("Phone Number:", self.phone_number)
        print("Emergency Contact:", self.emergency_contact)
        print()