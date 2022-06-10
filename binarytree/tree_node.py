from binarytree.device import Device


class Node:

    def __init__(self, value: Device) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: Device):

        if value == self.value:
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def delete_node(self, node: Device):

        if node < self.value:
            if self.left:
                self.left = self.left.delete_node(node)
        elif node > self.value:
            if self.right:
                self.right = self.right.delete_node(node)
        else:
            if self.left is None and self.right is None:
                del self
                return None
            elif self.left is None:
                temp = self.right
                del self
                return temp
            elif self.right is None:
                temp = self.left
                del self
                return temp

            min_val = self.right.find_min()
            self.value = min_val
            self.right = self.right.delete_node(min_val)

        return self

    def delete_all_by_year(self, year: int):
        el_to_delete = self.search_by_year(year)
        for el in el_to_delete:
            self.delete_node(el)

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def search_by_year(self, year):
        found = []
        if self.value.year_of_manufacture == year:
            found.append(self.value)
        if self.left:
            found += self.left.search_by_year(year)
        if self.right:
            found += self.right.search_by_year(year)
        return found

    def print_all_qt_limit(self, limit):
        if self.value.measurement_limit >= limit:
            print(self.value)
        if self.left:
            self.left.print_all_qt_limit(limit)
        if self.right:
            self.right.print_all_qt_limit(limit)

    def do_preorder_traversal(self):
        elements = [self]

        if self.left:
            elements += self.left.do_preorder_traversal()
        if self.right:
            elements += self.right.do_preorder_traversal()

        return elements

    def __str__(self):
        return self.value.__str__()


def delete_a_tree(node):
    if node is not None:
        delete_a_tree(node.left)
        delete_a_tree(node.right)
        node.left = node.right = None
