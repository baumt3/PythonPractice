cclass Procedure:
    def __init__(self, name, date, practitioner, cost):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.cost = cost

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_cost(self):
        return self.cost

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def set_cost(self, cost):
        self.cost = cost

    def display_info(self):
        print("Procedure Information:")
        print("Name:", self.name)
        print("Date:", self.date)
        print("Practitioner:", self.practitioner)
        print("Cost:", self.cost)
        print()