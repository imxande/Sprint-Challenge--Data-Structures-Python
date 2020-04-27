class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

 # Task 3. Reverse a Linked List Recursively
    def reverse_list(self, node, prev):
        # base case if there is not node
        if node is None:
            return
        # check if get next returns no value 
        if node.get_next() == None:
            # if so add the node to the head
            self.head = node
            # next has to be the previous now
            self.head.next_node = prev
            return
        # passing the node as the next and passing the prev as node
        self.reverse_list(node.get_next(), node)
        # next of the node will be the previous
        node.next_node = prev
       
       
        
