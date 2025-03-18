# Linked list
# Singly linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Usage
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.display()  # Output: 10 -> 20 -> 30 -> None

# ////////////////////////////////////////////////////////////////////
# Reverse LinkedList

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)

# reversed_head = reverse_linked_list(head)
# while reversed_head:
#     print(reversed_head.val)
#     reversed_head = reversed_head.next

