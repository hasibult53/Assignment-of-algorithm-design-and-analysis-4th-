class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.sibling = None
        self.degree = 0

class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        head = None
        prev = None
        next = None

        while h1 is not None and h2 is not None:
            if h1.degree <= h2.degree:
                next = h1
                h1 = h1.sibling
            else:
                next = h2
                h2 = h2.sibling

            if prev is None:
                head = next
            else:
                prev.sibling = next

            prev = next

        if h1 is not None:
            prev.sibling = h1
        elif h2 is not None:
            prev.sibling = h2

        return head

    def insert(self, key):
        x = Node(key)
        self.head = self.merge(self.head, x)

    def findMin(self):
        if self.head is None:
            return None

        min = self.head
        ptr = self.head
        while ptr is not None:
            if ptr.key < min.key:
                min = ptr
            ptr = ptr.sibling

        return min.key

    def extractMin(self):
        if self.head is None:
            return None

        prev = None
        ptr = self.head
        minNode = self.head
        while ptr is not None:
            if ptr.key < minNode.key:
                minNode = ptr
                prev = ptr
            ptr = ptr.sibling

        if prev is not None:
            prev.sibling = minNode.sibling
        else:
            self.head = minNode.sibling

        trees = minNode.child
        self.head = self.merge(self.head, trees)
        return minNode.key

# Example usage:
heap = BinomialHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)

print("Minimum element:", heap.findMin())
print("Extracted minimum:", heap.extractMin())
print("Minimum element after extraction:", heap.findMin())
