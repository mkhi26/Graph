class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.first = None

    def push(self, value, position=-1):
        if not self.first:
            self.first = Node(value)
            return True
        current = self.first
        if position == 0:
            self.first = Node(value)
            self.first.next = current
            return True
        previous = self.first
        current = self.first.next
        count = 1
        while current:
            if count == position:
                previous.next = Node(value)
                previous.next.next = current
                return True
            count += 1
            previous = current
            current = current.next
        previous.next = Node(value)
        return True

    def lsPrint(self):
        current = self.first
        text = ""
        while current:
            text += "%s->" % (current.value)
            current = current.next
        text += "null"
        return text

    def pop(self, position=0):
        if not self.first:
            return None

        if position == 0:
            delete = self.first
            self.first = self.first.next
            return delete.value
        count = 1
        previous = self.first
        current = self.first.next
        while current:
            if count == position:
                previous.next = previous.next.next
                return current.value
            count += 1
            previous = current
            current = current.next
    def exists(self, value, comparissonFun):
        current = self.first
        while current:
            if comparissonFun(current, value):
                return True
            current = current.next
        return False


    def get(self, value, comparissonFun):
        current = self.first
        while current:
            if comparissonFun(current, value):
                return current
            current = current.next
        return None




    def size(self):
        current = self.first
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def __str__(self):
        return self.lsPrint()

    def __len__(self):
        return self.size()
    def print(self, fun):
        result = []
        current = self.first
        while current:
            result += [fun(current)]
            current = current.next
            result += ["None"]
        return "->".join(result)

