'''Trinary Tree'''
class TrinaryTree:
    '''Trinary Tree'''

    def __init__(self, data=None):
        self.left = None
        self.middle = None
        self.right = None
        self.data = data

    def insert_root(self, data, right):
        '''Insert root'''
        self.left = None
        self.middle = None
        self.right = TrinaryTree(right)
        self.data = data

    def search(self, value):
        '''Search'''

        if not self.data:
            return False

        curr = self
        while curr.data:
            try:
                if curr.data == value:
                    return True
                if value < curr.data:
                    curr = curr.left
                else:
                    if value < curr.right.data:
                        curr = curr.middle
                    else:
                        curr = curr.right
            except:
                return False

        return False


    def search_recurr(self, value):
        '''Search recursively'''

        if not self.data:
            return

        if value == self.data:
            return True

        if value < self.data and self.left \
            and self.left.search_recurr(value):
            return True

        if self.middle \
            and self.middle.search_recurr(value):
            return True

        if value > self.data and self.right \
            and self.right.search_recurr(value):
            return True

        return False



    def insert(self, data):
        '''Insert'''

        if self.data:

            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = TrinaryTree(data)

            else:
                if self.right:
                    if data > self.right.data:
                        self.right.insert(data)
                    else:
                        if self.middle:
                            self.middle.insert(data)
                        else:
                            self.middle = TrinaryTree(data)
                else:
                    if self.middle:
                        if data > self.middle.data:
                            self.right = TrinaryTree(data)
                    else:
                        self.right = TrinaryTree(data)

        else:
            TrinaryTree(data)

    def in_order_traversal(self, root):
        '''In order reversal'''

        res = []

        if root:
            res += self.in_order_traversal(root.left)
            res.append(root.data)
            res +=  self.in_order_traversal(root.middle)
            res += self.in_order_traversal(root.right)

        return res


    def pre_order_traversal(self):
        '''Pre Order Traversal'''

        res = []

        if self:
            res.append(self.data)
            res += self.in_order_traversal(self.left)
            res += self.in_order_traversal(self.middle)
            res +=  self.in_order_traversal(self.right)

        return res


    def post_order_traversal(self):
        '''Post order Traversal'''

        res = []

        if self:
            res += self.in_order_traversal(self.left)
            res +=  self.in_order_traversal(self.middle)
            res +=  self.in_order_traversal(self.right)
            res.append(self.data)

        return res

if __name__ == '__main__':
    root = TrinaryTree(8)
    root.insert(10)
    root.insert(3)
    root.insert(6)
    root.insert(1)
    root.insert(14)
    in_order_res = root.in_order_traversal(root)
    print(in_order_res)

    pre_order_res = root.pre_order_traversal()
    print(pre_order_res)

    post_order_res = root.post_order_traversal()
    print(post_order_res)

    print(root.search(7))
    print(root.search_recurr(14))
