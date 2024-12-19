from colorama import *
from enum import Enum
import os 
import json

students = []
last_id= 0


class Actions(Enum): 
    EXIT = 0 
    ADD =  1 
    FIND = 2 
    DELETE = 3 
    UPDATE = 4 
    DISPLAY = 5
def clear_terminal ():
        os.system('clear') 

def menu():
    for opt in Actions: print(Fore.BLUE + Style.BRIGHT + str(f"{opt.value} -- {opt.name}"))
    return input("Choose action to proceed:")

def add_student ():
      save_into_json_file()
      global last_id
      last_id +=1

        
      students.append({ 'id' : last_id,
                       'name' : input(Fore.GREEN+'Full Name:'),
                       'age' : input(Fore.GREEN+"Age:"),
                       'gender' : input(Fore.GREEN+"Gender:")})  
 
      write_into_json_file() 
      return

def display_students():
     save_into_json_file()
     if not students:
        print(Fore.RED + "No students found.")
        return
     for stu in students:
        print(Fore.MAGENTA + f"Full Name: {Fore.GREEN +stu['name']},{Fore.MAGENTA} Age: {Fore.GREEN+ stu['age']},{Fore.MAGENTA} Gender: {Fore.GREEN+stu['gender']}")
          

def write_into_json_file():
        FILE_NAME = 'students.json'
        with open(FILE_NAME, 'w+') as f:
            json.dump(students,f, indent= 4)
        

def save_into_json_file():
        global students
        FILE_NAME = 'students.json'
        try:
            with open(FILE_NAME, 'r+') as f:
                students = json.load(f)

        except: print("error")

def find_student ():
     save_into_json_file()
     exist = False
     student_name = input(Fore.YELLOW + "Student Name: ")
     for stu in students:
          if student_name == stu['name']: 
            print(Fore.MAGENTA + f"Full Name: {Fore.GREEN}{stu['name']}, {Fore.MAGENTA}Age: {Fore.GREEN}{stu['age']}, {Fore.MAGENTA}Gender: {Fore.GREEN}{stu['gender']}")
            exist = True
            break
          if not exist:
            print(Fore.RED + "No students found.")
            break

def delete_student():
     save_into_json_file()
     student_name = input(Fore.RED + "Delete Student")
     deleted =False
     for stu in students:
          if student_name == stu['name']:
               students.remove(stu)
               print(Fore.RED + (f"{stu['name']} Deleted"))
               deleted=True
               write_into_json_file()
               break
     if not deleted:
          print(Fore.RED + "No student found")

def update_student_details():
     save_into_json_file()
     exist = False
     student_to_update = int(input("Choose student id: "))

     for stu in students:
        print(Fore.MAGENTA + f"Student id:{Fore.GREEN +str(stu['id'])},{Fore.MAGENTA}Full Name: {Fore.GREEN +stu['name']},{Fore.MAGENTA} Age: {Fore.GREEN+ stu['age']},{Fore.MAGENTA} Gender: {Fore.GREEN+stu['gender']}")
        if student_to_update == stu['id']:
                exist = True
                stu['name'] = input(Fore.GREEN + 'Full Name: ')
                stu['age'] = input(Fore.GREEN + "Age: ")
                stu['gender'] = input(Fore.GREEN + "Gender: ")
                print(Fore.GREEN + "Student details updated.")
                break
     write_into_json_file()
     if not exist: print(Fore.RED + "No student found")

        


     
    #  print({Fore.MAGENTA} + f"""Student id:{Fore.GREEN +str(stu['id'])},
    #           {Fore.MAGENTA} Full Name: {Fore.GREEN +stu['name']},
    #           {Fore.MAGENTA} Age: {Fore.GREEN+ stu['age']},
    #           {Fore.MAGENTA} Gender: {Fore.GREEN+stu['gender']}""")
         
