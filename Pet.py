# Create a class called Pet
class Pet:
    # The __init__ method will initialize the name, type, and age attributes
    def __init__(self, Animal_Name, Animal_Type, Animal_Age):
        # Create the instance variables that will store the information provided by the user.
        self.Animal_Name = Animal_Name
        self.Animal_Type = Animal_Type
        self.Animal_Age = Animal_Age

    # Use the accessor methods to retrieve the attribute values.
    def get_Animal_Name(self):
        return self.Animal_Name

    def get_Animal_Type(self):
        return self.Animal_Type

    def get_Animal_Age(self):
        return self.Animal_Age
