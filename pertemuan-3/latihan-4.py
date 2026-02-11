def merge_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    temp = list1.head
    while temp.next:
        temp = temp.next
    temp.next = list2.head
    return list1