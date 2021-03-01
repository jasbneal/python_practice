class Employee:
# Employee class that stores the name, ID number, department and job title data attributes.

    def __init__(self, name, ID_number, dept, title):
        self.__name = name
        self.__ID_number = ID_number
        self.__dept = dept
        self.__title = title
    
    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_dept(self, dept):
        self.__dept = dept
    
    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name
    
    def get_ID_number(self):
        return self.__ID_number

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    def __str__(self):
        return 'Employee Name: ' + self.__name + \
        '\nEmployee ID Number: ' + str(self.__ID_number) + \
        '\nEmployee Dept: ' + self.__dept + \
        '\nEmployee Title: ' + self.__title