class Employee():
    """员工类"""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, prompt=5000):
        self.salary = self.salary + prompt
