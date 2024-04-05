class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:

    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        if(current_node.get_value() == value_to_remove):
            self.head_node = current_node.get_next_node()
        else:
            while(current_node):
                next_node = current_node.get_next_node()
                if(next_node.get_value() == value_to_remove):
                    current_node.set_next_node(next_node.get_next_node())
                    
                    #Remove reference to node held in current node
                    current_node = None
                else:
                    current_node = next_node

    def remove_nodes(self, values_as_list):
        for value in values_as_list:
            self.remove_node(value)
            
    def printList(self, show_nodes=False):
        output = "(HEAD) "
        current_node = self.head_node
        while(current_node):
            if(current_node.get_value() != None):
                output += str(current_node.get_value())
                if(current_node.get_next_node() != None and show_nodes):
                    output += " -> "
            current_node = current_node.get_next_node()
        output += " (TAIL)"
        return output


print("Inserting Node...")

list = LinkedList(5)
list.insert_beginning(20)
list.insert_beginning(100)
list.insert_beginning(500)
list.insert_beginning(2000)
list.insert_beginning(3000)
list.insert_beginning(800)
list.insert_beginning(4000)
list.insert_beginning(5000)
print(list.printList(True))

print("Removing Node...")
list.remove_node(100)
list.remove_node(2000)
print("Removing Nodes...")
list.remove_nodes([800, 500, 3000])
print(list.printList(True))
