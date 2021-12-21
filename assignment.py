class Assignment:
    def __init__(self, title, description, sub_date_time, oral_mark, total_mark):
        self.title = title
        self.description = description
        self.sub_date_time = sub_date_time
        self.oral_mark = oral_mark
        self.total_mark = total_mark

    def __str__(self):
        return f"Title: {self.title} Descript: {self.description} Until: {self.sub_date_time} Oral: {self.oral_mark} Total: {self.total_mark}"