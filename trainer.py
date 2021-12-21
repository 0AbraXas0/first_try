class Trainer:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def __str__(self):
        return f"First: {self.first_name} Last: {self.last_name} Teaches: {self.subject}"