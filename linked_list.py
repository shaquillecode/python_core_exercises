""" 
Implementation of a Linked List 

Improvements to make:

1) make sure insert doesn't insert the same value twice (no duplicates)
2) returns all the data as one long string from linkedlist -> abcd
3) implement delete


"""

class Node:
    def __init__(self, data, start= True):
        self.data = data
        self.nextval = None
        self.prev = None
        self.start = start

    def __str__(self):
        return f"NODE({self.data})"


class NodeTwoPointers(Node):

    def __init__(self, data):
        self.prev = None
        self.data =  data

class LinkedList:


    SEPARATOR = "->"
    CAPACITY = 5

    def __init__(self):
        self.head = None


    def safety_check(self, node):
        """ 

        private method check if insert is possible
        throw an exception if other wise
        """
        if self.is_full():
            raise Exception(f"{node} Capacity exceeded, Insert Failed!")

        if self.contains(node.data):
            raise Exception(f"{node} already present! Insert Failed!") 



    def push(self, node):

        if not self.is_full():
            node.nextval = self.head 
            self.head = node
        else:
            raise Exception("Linked List already full! pushed Failed")


    def insert(self, node):
        """ 
        param: Node
        return: None
        Inserts a node into the linked list (At the end of the list)
        """

        # covers the case where the linked list is empty


        # if not self.head  == if self.head is None
        if self.is_empty():
            self.head = node
        else:
            self.safety_check(node)
            curr = self.head
            while curr.nextval:
                curr = curr.nextval
            curr.nextval = node


    def delete(self, val):

        """ 
        param: string
        return: None

        delete a value from the linked list

        """

        deleted = False
        if self.is_empty():
            return
        else:

            curr = self.head

            # handle the case that it's at the front of the list
            if curr.data == val:
                self.head = curr.nextval
                return

            # otherwise look through the list
            while curr:
                if curr.nextval.data == val:
                    curr.nextval = curr.nextval.nextval
                    break
                curr = curr.nextval



    def contains(self, val):

        """ 
        param: string
        return: boolean

        Checks if a value exists in the list 
        """

        if self.is_empty():
            return False
        else:
            curr = self.head

            # check if first element 
            # is equal to the value we are looking for

            # iterate through the linked list looking for the value
            while curr:
                if curr.data == val:
                    return True 
                curr = curr.nextval

        return False


    def length(self, MAX = 5):
        """ 

        param: None
        return: int

        Gets the length of the linked list
        """

        counter = 0

        if not self.head:
            return counter
        else:
            curr = self.head

            while curr:
                counter += 1
                curr = curr.nextval

        return counter

    def is_empty(self):

        """ 
        param: none
        return: boolean
        Checks if the linked list is empty
        """

        if not self.head:
            return True
        return False

    def is_full(self):
        """ 
        param: none
        return: boolean
        Checks if the linked list is empty
        """
        if self.length() == self.CAPACITY:
            return True 
        return False



    def __str__(self):

        res = str()

        if not self.head:
            return "List is empty"
        else:
            curr = self.head 
            while curr:
                #add data to the string representation
                res += curr.data

                # only add an arrow when there is a next element
                if curr.nextval:
                    res += self.SEPARATOR

                # set the next element equal to curr (AKA: iterate)
                curr = curr.nextval

        return res


class DoublyLinkedList(LinkedList):
    SEPARATOR = "<->"


    def insert(self, node):

        if self.is_empty():
            self.head = node
        else:
            self.safety_check(node)
            curr = self.head
            while curr.nextval:
                curr = curr.nextval

            curr.nextval = node
            node.prev = curr


    def push(self, node):

        self.safety_check()
        node.nextval = self.head
        self.head = node 

    def delete(self):
        """ 
        param: string
        return: None

        delete a value from the linked list

        """

        deleted = False
        if self.is_empty():
            return
        else:

            curr = self.head

            # handle the case that it's at the front of the list
            if curr.data == val:
                self.head = curr.nextval
                return

            # otherwise look through the list
            while curr:
                if curr.nextval.data == val:
                    curr.nextval = curr.nextval.nextval
                    curr.nextval.prev = curr
                    break
                curr = curr.nextval

class CircularDoublyLinkedList(LinkedList):
	pass




if __name__ == '__main__':

    list1  = LinkedList()

    list_d = DoublyLinkedList() 

    #node1_d = Node("A")
    #print(node1_d)

    #list_d.insert(node1_d)

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")

    list1.insert(node1)
    list1.insert(node2)
    list1.insert(node3)

    list_d.insert(node4)
    list_d.insert(node5)
    list_d.insert(node6)

    print(list_d)
    print(list1)
    list1.insert(node4)
    # list1.insert(node5)
    # list1.push(node6)
    #list1.insert(node6)
    print(list1)
    print(list_d)

    # print(list1.contains("B"))
    # print(list1.contains("A")) 

    # print(list1)

    # list1.delete("B")

    # print(list1)
    # print(list1.length()) 


    # A -> None
    # A -> B -> None
    # A -> B -> C


    # print(f"head of list: {list1.head}")
    # print(f"first element of list1: {list1.head.nextval}")
    # print(f"second element of list1: {list1.head.nextval.nextval}")
    # print(f"second element of list1: {list1.head.nextval.nextval.nextval}")