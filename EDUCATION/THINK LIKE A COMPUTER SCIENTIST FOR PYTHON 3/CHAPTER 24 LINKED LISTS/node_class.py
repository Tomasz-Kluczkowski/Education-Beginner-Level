class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        if self.cargo == None:
            return ""
        return str(self.cargo)

    def print_backward(self):
        first_node = self
        if self.next is not None: #if not last item which does not have next defined
            tail = self.next      #move to the next item, print nothing
            tail.print_backward() #call to print tail recursively until we reach
        print(self.cargo, end=" ") #print item with no next defined
        if self is not first_node:
            print(",", end=" ")