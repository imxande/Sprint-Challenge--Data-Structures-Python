import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
        else: 
            # if not right node
            if not self.right: 
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if value is equal to the target return true
        if self.value == target:
            # return true 
            return 1

        # if target less than the value
        if target < self.value:
            # if not left node 
            if not self.left:
                # return false 
                return 0
            else: 
                return self.left.contains(target)
        else: 
            if not self.right:
                # return false 
                return 0
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: 
            return self.value
        else: 
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # calling cb on the value
        cb(self.value)

        # if there is left node 
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # Print all the values in order from low to high
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right) 