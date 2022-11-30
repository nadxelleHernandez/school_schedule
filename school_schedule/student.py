class Student():
    def __init__(self, name, grade, classes):
        if not name or not grade or classes is None:
            raise ValueError("Invalid parameters while creating Student object")

        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        if class_name:
            self.classes.append(class_name)

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"
