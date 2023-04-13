#import data structure
import DATA_STRUCTURE as DS
#write function
#D. MY PERSON
class my_person():
    def __init__(self):
        self.mytree =DS.my_BSTree()
    def load(self):
        self.employee_tree = None
        input_link =  input("Please enter your file path:")
        try: data_file = open(input_link, "r") 
        except:
            print("File-path is not correct")
            data_file = None
        if data_file is not None:
            data_list = data_file.readlines()
            for data in data_list:
                data =  data.strip("\n").split(",")
                #employee id
                id =  int(data[0])
                #employee name
                name=  data[1]
                #employee birth place
                birth_place = data[2]
                #employee birth day
                birth_day =  data[3]
                #create node
                add_person =  DS.person(id, name,birth_day, birth_place)
                self.employee_tree = self.mytree.insert_AVL(self.employee_tree,add_person)
            print("Load file successfully")
    def insert_person(self):
        #input id
        id = -1
        while id < 0: 
            try: id  =  int(input("Please input ID of new employee: "))
            except:
                print("You input wrong data type, please input numer")
                continue
            if id < 0:
                print("You input minus value, please re-enter")
                continue
                #check if ID has been used or not
            existance =  self.mytree.search_BST(self.employee_tree,id)
            if existance is not None:
                print("ID has been chosen, please input another ID")
                continue             
        #input new employ's name
        name = input("Please enter new employee's name: ") 
        #Input new employee's birthdate
        DOB = input("Please enter new employee's birthdate: ") 
        #Input new employee's Birth place
        birth_place =  input("Please enter new employee's birth place: ")
        new_employee =  DS.person(id, name, DOB, birth_place)
        self.employee_tree = self.mytree.insert_AVL(self.employee_tree, new_employee)
        print("New ID:", id)
        print("New name:", name)
        print("Birth place: ", birth_place)
        print("Day of birth:", DOB)   
        #save to file
        self.save2file() 
    def Inoder_traversal(self):
        aws = self.mytree.inorder_traverse(self.employee_tree)
        print("lens",len(aws))
        print("{:^8}""|{:^16}""|{:^16}""|{:^16}".format("ID","Name ","Day of birth", "Birth place"))
        for person in aws:
            person.print_person()
    def search_ID(self):
        id =  -1 
        while id <0:
            try: id = int(input("Please input searching ID:"))
            except:
                print("You input wrong type of ID, please input number")
                continue
            if id <= -1:
                print("You input minus value, please re-enter searching ID:")
        aws = self.mytree.search_BST(self.employee_tree,id)
        if aws is None:
            print("The searcher ID is not valid")
        else:
            print("{:^8}""|{:^16}""|{:^16}""|{:^16}".format("ID","Name ","Day of birth", "Birth place"))
            aws.print_person()
        return aws
    def delete_ID(self):
        #searching result
        del_person = self.search_ID()
        if del_person is not None:
            self.employee_tree = self.mytree.delete_AVL(self.employee_tree, del_person)
            print("Delete successfully")
            self.save2file()
    def save2file(self):
        #print("Do you want to save your change?\n0:NO\n1:YES")
        select = -1
        while select <0 or select > 1:
            print("Do you want to save your change?\n0:NO\n1:YES")
            try: select = int(input("Please enter your selection:"))
            except:
                print("You input wrong selection")
                continue
            if select >1 or select <0:
                print("You input wrong selection")
                continue
        if select ==1:
            #using inorder traversal to write data from smallest ID number
            data2save =  self.mytree.inorder_traverse(self.employee_tree)
            #input link that you want to save file
            output_link = input("Please enter output file path:")
            with open(output_link,"w") as output_file:
                for person in data2save:
                    output_file.write(str(person.id)+","+ person.name+","+person.birth_place+","+ person.DOB+"\n")
            print("Data has been save successfully")
    def edit_information(self):
        id =  -1 
        while id <0:
            try: id = int(input("Please input searching ID:"))
            except:
                print("You input wrong type of ID, please input number")
                continue
            if id <= -1:
                print("You input minus value, please re-enter searching ID:")
        edit_person = self.mytree.edit(self.employee_tree,id)
        #print new information
        if edit_person is not None:
            print("{:^8}""|{:^16}""|{:^16}""|{:^16}".format("ID","Name ","Day of birth", "Birth place")) 
            edit_person.print_person()  
            self.save2file()
        else:
            print("The searching ID is not exist")      