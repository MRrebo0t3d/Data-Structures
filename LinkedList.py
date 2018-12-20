"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head:
            pointer_val = self.head
            pos = 1
            if position < 1:
                return None
            while pointer_val and pos < position:
                pointer_val = pointer_val.next
                pos += 1
                if pos == position:
                    return pointer_val
                if pointer_val:
                    continue
                else:
                    break
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        curr_pos = 1
        val = self.head
        if position > 1:
            while val and curr_pos < position:
                if curr_pos == position - 1:
                    new_element.next = val.next
                    val.next = new_element
                val = val.next
                curr_pos += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current.value = curr_val.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        pass


# Test cases
# Set up some Elements
e1 = Element(3)
e2 = Element(6)
e3 = Element(9)
e4 = Element(12)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
