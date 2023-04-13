#data structure
#A.CLASS PERSON1
class person():
    #DOB: date of Birth
    def __init__(self, id, name, DOB, Birth_place):
        #employee'id
        self.id = id
        #employee's name
        self.name = name
        #employee's date of birth
        self.DOB = DOB
        #employee's birth place
        self.birth_place =  Birth_place
        #self.left =  None 
        #self.right =  None
    def print_person(self):
        print("{:^8}""|{:^16}""|{:^16}""|{:^16}".format(self.id,self.name, self.DOB,self.birth_place))
#B.MYQUEUE
class my_queue():
    def __init__(self):
        self.queue =  []
        self.head = None
        self.tail =  None
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        return self.queue.pop(0)
#C.MY BS TREE
class treenode():
    def __init__(self, person):
        self.left = None 
        self.right = None
        self.node =  person
class my_BSTree():
    def insert(self,root,node):
        if root is None:
            root =  treenode(node)
        else:
            if node.id < root.node.id:
                if root.left is None:
                    root.left = treenode(node)
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right =  treenode(node)
                else:
                    self.insert(root.right,node)
    
    def get_heights(self,root):
        if root is None:
            return -1
        elif root.left is None and root.right is None:
            return 0
        else:
            return 1+ max(self.get_heights(root.left), self.get_heights(root.right))
    def get_balance(self,root):
        if root is None:
            return 0
        else:
            return self.get_heights(root.left)-self.get_heights(root.right)
    def rotate_right(self,root):
        #determin new root node
        rotate_node = root.left
        rotate_brand =  root
        #perfome rotation
        rotate_brand.left =  rotate_node.right
        rotate_node.right = rotate_brand
        return rotate_node
    def left_rotate(self,root):
        #determine root node
        rotate_node = root.right
        #perform rotation
        rotate_brand =  root
        rotate_brand.right =  rotate_node.left
        rotate_node.left = rotate_brand
        #return new node
        return rotate_node
    def insert_AVL(self,root,person_node):
        if root is None :
            return treenode(person_node)
        else:
            if person_node.id < root.node.id:
                if root.left is None:
                    root.left = treenode(person_node)
                else:
                    root.left = self.insert_AVL(root.left,person_node)
            else:
                if root.right is None:
                    root.right = treenode(person_node)
                else:
                    root.right = self.insert_AVL(root.right,person_node)
            balance =  self.get_balance(root)
            #case left - left
            if balance > 1 and person_node.id < root.left.node.id:
                return self.rotate_right(root)
            #case left -right
            elif balance > 1 and person_node.id >root.left.node.id:
                root.left= self.left_rotate(root.left)
                return self.rotate_right(root)
            #case right - right
            elif balance < -1 and person_node.id > root.right.node.id:
                return self.left_rotate(root)
            #case righ -left
            elif balance < -1 and person_node.id < root.right.node.id:
                root.right =  self.rotate_right(root.right)
                return self.left_rotate(root)
        return root
    def inorder_traverse(self,root):
        res = []
        if root is not None:
            res = self.inorder_traverse(root.left)
            res.append(root.node)
            res = res+self.inorder_traverse(root.right)
        return res
    def search_BST(self,root,element):
        if root is None:
            return None
        else:
            if element == root.node.id:
                return root.node
            elif element <root.node.id:
                return self.search_BST(root.left, element)
            elif element > root.node.id:
                return self.search_BST(root.right, element) 
    #determin new root using for delete function
    def get_min(self, root):
        if root is None:
            return root
        else:
            if root.left is None:
                return root
            else:
                return self.get_min(root.left)
    def delete_AVL(self,root, person ):
        if root is None:
            return root
        elif person.id<root.node.id:
            root.left = self.delete_AVL(root.left, person)
        elif person.id > root.node.id:
            root.right =  self.delete_AVL(root.right, person)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp =  root.left
                root =  None
                return temp
            temp =  self.get_min(root.right)
            root.node =  temp.node
            root.right = self.delete_AVL(root.right, temp.node)
        #perform AVL tree
        balance =  self.get_balance(root)
        #left-left case
        if balance > 1  and self.get_balance(root.left) >= 0:
            return self.rotate_right(root.left)
        #left-right case
        elif balance >1 and self.get_balance(root.left ) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        #right-right case
        elif balance < -1 and self.get_balance(root.right) <=0:
            return self.left_rotate(root)
        #right-left case
        elif balance < -1 and self.get_balance(root.right):
            root.right =  self.rotate_right(root.right)
            return self.left_rotate(root)
        return root
    def edit(self,root,element):
            if root is None:
                return None
            else:
                if element == root.node.id:
                    #editnode
                    id_edit =  input("Please enter new id: ")
                    if len(id_edit) !=0 :
                        new_id = -1
                        while new_id <=0: 
                            try: new_id= int(id_edit)
                            except:
                                print("You input wrong data type, please input number")
                                id_edit = input("Please re-enter id number")
                                continue
                            if new_id <= 0:
                                print("You input minus value, please re-enter")
                                id_edit = input("Please re-enter value:")
                                continue
                        root.node.id =  new_id
                    name_edit =  input("Please enter new name: ")
                    if len(name_edit) !=0 :
                        root.node.name =  name_edit
                    birth_place_edit = input("Please enter new birth place: ")
                    if len(birth_place_edit) != 0:
                        root.node.birth_place =  birth_place_edit
                    DOB_edit  =  input("Please enter new date of birth: ")
                    if len(DOB_edit) != 0:
                        root.node.DOB= DOB_edit
                    return root.node                      
                elif element <root.node.id:
                    return self.edit(root.left, element)
                elif element > root.node.id:
                    return self.edit(root.right, element)
