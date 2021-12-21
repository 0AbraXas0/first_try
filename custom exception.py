class toDikoMouException(Exception):
    def __init__(self, salary, message="salary out of limits"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

class Worker:
    def __init__(name, position, salary):
        self.name = name
        self.position = position    
        if not 800 < salary < 1500:
            raise toDikoMouException(salary)
        else:
            self.salary = salary

mitsos = Worker("mitsos", 19, 1000)