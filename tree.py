"""
A Tree represents the nodes connected by edges.
It is a non-linear data structure. It has the following properties

One node is marked as root node
Every node other than the root is associated with one parent node.
Each node can have any amount of children nodes

"""
class Node:
    '''Tree'''

    def __init__(self, data):
        self.left = None
        self.right =  None
        self.data = data


    def __str__(self):
        return f"{self.data}"

def hasChildrenSumProperty(node):
    '''
    A Tree is a non-linear data structure.
    This Function will check if the Tree
    has the following properties:
    The sum of the Child nodes will equal the Parent Node
    OR Return False
    '''

    if not node or (not node.left and not node.right):
        return True

    else:
        if node.left:
            left = node.left

        if node.right:
            right = node.right

        if((node.data == left.data + right.data) and hasChildrenSumProperty(left)
        and hasChildrenSumProperty(right)):
            return True
        return False

if __name__ == '__main__':
    root = Node(25)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(hasChildrenSumProperty(root))
    print("==="*35)

class Tree:
    '''Tree'''

    def __init__(self, data):
        self.left = None
        self.right =  None
        self.data = data


    def in_order_traversal(self, root2):
        '''In order'''
        res = []

        if root2:
            res += self.in_order_traversal(root2.left)
            res.append(root2.data)
            res +=  self.in_order_traversal(root2.right)
        return res


    def pre_order_traversal(self):
        '''Pre order'''
        res = []

        if root2:
            res.append(root2.data)
            res += self.in_order_traversal(root2.left)
            res +=  self.in_order_traversal(root2.right)
        return res


    def post_order_traversal(self):
        '''Post'''
        res = []

        if root2:

            res += self.in_order_traversal(root2.left)
            res +=  self.in_order_traversal(root2.right)
            res.append(root2.data)
        return res


    def insert(self, data):
        '''Insert'''

        if self.data:


            # i.e. 3 < 8
            if data < self.data:

                if not self.left:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)

            # i.e. 10 > 8
            elif data > self.data:

                if not self.right:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data


    def __str__(self):
        return f"{self.data}"

    def search(self,data):
        '''Search'''
        if data in self.in_order_traversal(self):
            return True
        return False

    def get_level(self):
        '''Get level'''
        depth = 0
        if self.left:
            depth = max(depth, self.left.get_level())
        if self.right:
            depth = max(depth, self.right.get_level())
        return depth +1

    def print_all(self,data):
        '''Print all'''
        if root2:
            print(data)
            print(root2.left.right)
            # for i in data:
            #     print(i)

    def find_path(self, val, path=[]):
        '''Find Path'''

        if self.data == val:
            print(path)
            return

        if self.left:
            path.append(self.left.data)
            self.left.find_path(val, path)

        if self.right:
            path.append(self.right.data)
            self.right.find_path(val, path)
        return path



if __name__ == '__main__':
    root2 = Tree(8)
    root2.insert(10)
    root2.insert(3)
    root2.insert(6)
    root2.insert(1)
    root2.insert(14)

    res = root2.in_order_traversal(root2)
    print(res)

    pre_order_res = root2.pre_order_traversal()
    print(pre_order_res)

    post_order_res = root2.post_order_traversal()
    print(post_order_res)

    print(root2.search(6))
    print(root2.find_path(1))
