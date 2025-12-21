def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index")

    current = node
    count = 0

    while count < index:
        current = current.next
        if current is None:
            raise Exception("Invalid index")
        count += 1

    return current