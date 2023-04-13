import FUNCTION as my_employee
class main():
    def __init__(self):
        self.manage = my_employee.my_person()
    def operation(self):
        while 1==1:
            print("+-------------------Menu--------------------+")
            print("1. Load data from the file")
            print("2. Insert a new Person")
            print("3. Inorder traverse")
            #print("3. Display Employee Information")
            print("4. Search by Person ID")
            print("5. Delete by Person ID")
            print("6. Edit employee information")
            print("7. Save to file")
            print("0. Exit")
            print("+-------------------Menu--------------------+")
            #Enter selection
            selection = None
            while selection is None:
                select_str = input("Please enter your selection:")
                try: selection = int(select_str)
                except:
                    print("You input wrong type, please input number")
                    continue
                if selection <= -1:
                    print("You input minus number, please re-input your selection")
                    selection = None
                    continue
            #load data from file
            break_char = None 
            #selection 0 to quit
            if selection ==0:
                break
            while break_char is None:
                #Load data from file
                if selection == 1:
                    self.manage.load()
                #add new employee         
                elif selection == 2:
                    self.manage.insert_person()
                #inoder traverse
                elif selection == 3:
                    self.manage.Inoder_traversal()
                #Breath-First Search traverse
                #elif selection == 4:
                #    self.manage.BFS_traversal()
                #Search by ID
                elif selection == 4:
                    self.manage.search_ID()
                #delete employee by ID
                elif selection == 5:
                    self.manage.delete_ID()
                elif selection ==6:
                    self.manage.edit_information()
                elif selection ==7:
                    self.manage.save2file()
                #set break char to turn back menu
                break_char = input("Please type anything to back to menu")
        
a = main().operation()