# Rebecca Essenburg
# Assignment 8.2
# 2/22/26

# This code will open and read a json file
# and then update that file with a new entry.

# Import necessary libraries.
import json

# Define Student class.
class Student:
    def __init__(self, F_Name,L_Name,Student_ID,Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

# Create class Decoder.
class StudentDecoder(json.JSONDecoder):
    def __init__(self, object_hook=None, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    def object_hook(self, o):
        decoded_student = Student(
            o.get('F_Name'),
            o.get('L_Name'),
            o.get('Student_ID'),
            o.get('Email'),
        )
        return decoded_student
    
# Create class Encoder.
class StudentEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,Student):
            return {
                    'F_Name': o.F_Name,
                    'L_Name': o.L_Name,
                    'Student_ID': o.Student_ID,
                    'Email': o.Email
                }
        else:
            return super().default(o)

# Create function to loop through object list and print.
def Print_Students(obj_list):
    for person in obj_list:
        print(f'{person.L_Name},{person.F_Name}: ID = {person.Student_ID}, Email = {person.Email}')

def main():
    # Load Student JSON file into a list of class objects.
    with open('Student.json','r') as f:
        student_list = json.load(f, cls=StudentDecoder)

    # User notif - Original list.
    print('This is the original list of Students:')
    # Call print function.
    Print_Students(student_list)
    print()

    # Add my info to list.
    my_student = Student("Rebecca","Essenburg",86753,"rebecca.essenburg@my365.bellevue.edu")
    student_list.append(my_student)
    # User notif - Updated list.
    print('This is the updated list of Students:')
    # Call print function.
    Print_Students(student_list)
    print()

    # Dump new info to JSON file.
    with open('Student.json','w') as f:
        json.dump(student_list,f, cls=StudentEncoder, indent=4)
    # User notif - File Updated.
    print("The 'Student' file has been updated.")

# Call main function.
if __name__ == '__main__':
    main()