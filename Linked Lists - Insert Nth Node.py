class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    new_node = Node(data)

    if index == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(index - 1):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head