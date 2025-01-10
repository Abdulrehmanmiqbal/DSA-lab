class Element:
    def __init__(self, data=0, next_element=None):
        self.data = data
        self.next_element = next_element

def invert_chain(start: Element) -> Element:
    if not start:
        return None

    temp_list = []

    current = start
    while current:
        temp_list.append(current.data)
        current = current.next_element

    reversed_head = Element(temp_list.pop())
    current = reversed_head

    while temp_list:
        current.next_element = Element(temp_list.pop())
        current = current.next_element

    return reversed_head

def print_chain(head: Element):
    current = head
    while current:
        print(current.data, end=" -> " if current.next_element else "")
        current = current.next_element
    print()

# Example Usage
start = Element(1, Element(2, Element(3, Element(4, Element(5)))))
new_head = invert_chain(start)
print_chain(new_head) 
