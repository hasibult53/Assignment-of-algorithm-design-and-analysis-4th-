class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "Red"  # All nodes are initially red

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.root.color = "Black"  # Root node is always black

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        # Fix violations after insertion
        node = self._fix_violation(node)
        return node

    def _fix_violation(self, node):
        # Case 1: Parent of red-red node is black
        if node is None or node.color == "Black":
            return node

        # Case 2: Both children of red-red node are red
        if node.left is not None and node.left.color == "Red" and \
           node.right is not None and node.right.color == "Red":
            self._flip_colors(node)
            return node

        # Case 3: Left child of red-red node is red, right child is black
        if node.left is not None and node.left.color == "Red" and \
           (node.right is None or node.right.color == "Black"):
            node = self._rotate_right(node)

        # Case 4: Right child of red-red node is red, left child is black
        if node.right is not None and node.right.color == "Red" and \
           (node.left is None or node.left.color == "Black"):
            node = self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = "Red"
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = "Red"
        return x

    def _flip_colors(self, node):
        node.color = "Black"
        node.left.color = "Black"
        node.right.color = "Black"

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node is not None:
            self._inorder_traversal_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_traversal_recursive(node.right)

# Example usage:
tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

print("Inorder traversal:")
tree.inorder_traversal()
