import datetime

class StudentAccount:
    def __init__(self, name, id, email, total_marks):
        self.name = name
        self._id = id
        self.__email = email
        self.__total_marks = total_marks

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'ID: {self._id}')
        print(f'Marks: {self.__total_marks}')
        print("Passed:", "Yes" if self.has_passed() else "No")

    @property
    def email(self):
        print("Email accessed at", datetime.datetime.now())
        return self.__email

    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self.__email = new_email
        else:
            print("New email is not valid!")

    @property
    def total_marks(self):
        return self.__total_marks

    @total_marks.setter
    def total_marks(self, new_marks):
        if 0 <= new_marks <= 500:
            self.__total_marks = new_marks
        else:
            print("Marks must be between 0 and 500")

    def has_passed(self):
        return self.__total_marks >= 250



a = StudentAccount("Emily", "1023", "emily@example.com", 300)
a.display_info()

print(a.email)  # Accessing email (with time)
a.total_marks = 460  # Updating marks with validation
print("Updated Marks:", a.total_marks)

