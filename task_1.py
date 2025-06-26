from rich import print

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next =Node(data)
    
    def print_list(self):   
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        return 
    
def get_middle(head):
    if head is None or head.next is None:
          return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sort(head):
    if not head or not head.next:
        return head 

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None  # Важливо! Тут ми розриваємо зв’язок

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    # Вибираю менше значення та рекурсивно з'єдную далі
    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

def print_sorted_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def merge_sorted_lists(head1, head2):
    # Створюємо фіктивний стартовий вузол
    dummy = Node()
    tail = dummy

    # Поки обидва списки не порожні
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # Додаємо залишок одного з двох списків
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next  # Повертаємо голову нового списку

   
if __name__ == "__main__":
    mylist = LinkedList()

    mylist.insert_at_end(23)
    mylist.insert_at_end(12)
    mylist.insert_at_end(34)

    print("До реверсу mylist:")
    mylist.print_list()

    mylist.reverse()

    print("Після реверсу mylist:")
    mylist.print_list()

    sorted_head = merge_sort(mylist.head)
    print("Після сортування злиттям mylist:")
    print_sorted_list(sorted_head)

    mylist_2 = LinkedList()
    mylist_2.insert_at_end(54)
    mylist_2.insert_at_end(23)
    mylist_2.insert_at_end(41)
    mylist_2.insert_at_end(8)

    sorted_head_2 = merge_sort(mylist_2.head)
    print("Після сортування злиттям mylist_2:")
    print_sorted_list(sorted_head_2)

    merged_head = merge_sorted_lists(sorted_head, sorted_head_2)
    print_sorted_list(merged_head)