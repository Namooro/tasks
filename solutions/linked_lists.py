# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    """
    Inverts the linked list
    """
    prev, curr = None, head
    while curr:
        next, curr.next, prev, curr = curr.next, prev, curr, curr.next
        curr = next
    head = prev
    return head


def remove_dups(head: ListNode):
    """
    Remove duplicates from linked list
    """
    if head is None:
        return
    current = head
    unique = {current.val}
    while current.next:
        if current.next.value in unique:
            current.next = current.next.next
        else:
            unique.add(current.next.value)
            current = current.next

    return head

