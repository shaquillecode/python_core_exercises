""" 
A Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties

One node is marked as Root node
Every node other than the root is associated with one parent node.
Each node can have any amount of children nodes

"""

import re


class Tree:

    def __init__(self, data):
        self.left = None 
        self.right =  None
        self.data = data


    # in order traversal
    # def print_tree(self, order='inorder'):


    # 	if order == 'inorder':
    # 		return self.__in_order_traversal()
    # 	elif order == 'postorder':
    # 		self.__post_order_traversal()
    # 	elif order == 'preorder':
    # 		self.__pre_order_traversal()


    def in_order_traversal(self, root):        
        res = []

        if root:
            res += self.in_order_traversal(root.left)
            res.append(root.data)
            res +=  self.in_order_traversal(root.right)
        return res


    def pre_order_traversal(self):
        res = []

        if root:
            res.append(root.data)
            res += self.in_order_traversal(root.left)
            res +=  self.in_order_traversal(root.right)
        return res


    def post_order_traversal(self):
        res = []

        if root:
            
            res += self.in_order_traversal(root.left)
            res +=  self.in_order_traversal(root.right)
            res.append(root.data)
        return res
        

    def insert(self, data):

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
        if data in self.in_order_traversal(self):
            return True
        return False
    
    def get_level(self):
        depth = 0
        if self.left:
            depth = max(depth, self.left.get_level())
        if self.right:
            depth = max(depth, self.right.get_level())   
        return depth +1
    
    def print_all(self,data):
        if root:
            print(data)
            print(root.left.right)
            for i in data:
                print(i)


def main():
    root = Tree(8)
    root.insert(10)
    root.insert(3)

    return root

if __name__ == '__main__':
	
    # nodes = [i for i in range(1, 11)]
    root = Tree(8)
    root2 = Tree(6)
    # root.insert(2)
    # root.insert(3)
    root.insert(10)
    root.insert(3)
    root.insert(6)
    root.insert(1)
    root.insert(14)

    res = root.in_order_traversal(root)
    print(res)
    
    print(root.left.right)
    
    print(root.search(6))
    print(root2.search(8))
    
    print(root.get_level())
    print(root2.get_level())
    
    print(root.print_all(res))

    
   
	# for idx, node in enumerate(nodes):
	# 	if idx % 2 == 0:
	# 		tree.insert(node)
	# 	else:
	# 		tree.insert(node, left=False)


	#tree.print_tree()


	# print(tree.left)

	# print(tree.right.right)