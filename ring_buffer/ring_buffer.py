from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

# Method adds elements to the buffer.
    def append(self, item):
        # place holders
        storage = self.storage
        capacity = self.capacity
        
        # chech if storage is smaller than capacity
        if len(storage) < capacity:

        # Wraps the item and inserts it as the new tail of the list.
            storage.add_to_tail(item)
        else:
            # if current or its pointer does not exist 
            if self.current == None or self.current.next == None:
                # we want to use the head
                self.current = self.storage.head
            else:
                # otherwise we use next
                self.current = self.current.next
            # we want the value to be the item passed
            self.current.value = item
            
# returns all of the elements in the buffer in a list in their given order
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # place holder
        head = self.storage.head

        # while head is not empty
        while head != None:
            # append its value to the list
            list_buffer_contents.append(head.value)
            # increment
            head = head.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
