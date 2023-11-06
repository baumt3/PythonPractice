# Create a class called Patient
class Procedure:
    # The __init__ method will initialize the full name, address, phone number, and emergency contact attributes
    def __init__(self, name, date, practitioner, cost):
        # Create the instance variables that will store the information provided by the user.
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.cost = cost

    # Use the accessor methods to retrieve the attribute values.
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_cost(self):
        return self.cost

    # Use the mutactor methods to change the attributes if needed
    def set_name(self, name):
        self.name = name

    def set_date(self, address):
        self.date = date

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def set_cost(self, cost):
        self.cost = cost

    # Display the information
    def display_info(self):
        print("Procedure Information:")
        print("Name:", self.name)
        print("Date:", self.date)
        print("Practitioner:", self.practitioner)
        print("Cost:", self.cost)
        print()