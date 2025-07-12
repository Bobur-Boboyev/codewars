def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count