class EmployeeManagementApplication:
    def __init__(self):
        pass

class Employee:
    def __init__(self, name, serial, schedule, vacation_days, location):
        self._name = name
        self._serial = serial
        self._schedule = schedule
        self._vacation_days = vacation_days
        self._location = location

    def __str__(self):
        print(f'Name: {self._name}')
        print(f'Type: {self.__class__.__name__}')
        print(f'Serial number: {self._serial}')
        print(f'Vacation days: {self._vacation_days}')
        print(f'Desk: {self._location}')

class PartTimer(Employee):
    def __init__(self, name, serial):
        super().__init__(name, serial, 'Part Time', 0, 'open workspace')

class FullTimer(Employee):
    def __init__(self, name, serial, vacation_days, location):
        super().__init__(name, serial, 'Full Time', vacation_days, location)

    def take_vacation(self):
        pass

class RegularEmployee(FullTimer):
    def __init__(self, name, serial):
        super().__init__(name, serial, 10, 'cube farm')
    pass

class Manager(FullTimer):
    def __init__(self, name, serial):
        super().__init__(name, serial, 14, 'private office')

    def delegate():
        pass

class Executive(Manager):
    def __init__(self, name, serial):
        super().__init__(name, serial)
        self._vacation_days = 20
        self._location = 'corner office'
        self._can_hire_fire = True

Employee('Hop', 10, 'FullTimer', 27, 'Airplane')
FullTimer('Josh', 4, 10, 'Cube')
PartTimer('Drake', 47)
RegularEmployee('James', 63)
Manager('Farquaad', 100)
Executive('Byron', 64)