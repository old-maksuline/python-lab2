from binarytree.device import Device
from binarytree.tree_node import Node, delete_a_tree


def create_tree(devices):
    root_node = Node(devices[0])
    for i in range(1, len(devices)):
        root_node.insert(devices[i])
    return root_node


def main():
    devices = [Device("Vici", "Multimeter", 2005, 87), Device("Acrel", "Ammeter", 2009, 80),
               Device("Vici", "Multimeter", 2005, 83), Device("Sunhokey", "Voltmeter", 2009, 70),
               Device("Acrel", "Voltmeter", 2007, 78), Device("Sunhokey", "Ammeter", 2006, 98),
               Device("Sunhokey", "Oscillograph", 2007, 85)]

    tree = create_tree(devices)

    print("==========Printing preorder traversal==========")
    preorder_tree = tree.do_preorder_traversal()
    for node in preorder_tree:
        print(node)

    print("==========Printing preorder traversal after deleting a node==========")
    tree.delete_node(devices[1])
    preorder_tree = tree.do_preorder_traversal()
    for node in preorder_tree:
        print(node)

    print("==========Printing preorder traversal after deleting a nodes with same year==========")
    tree.delete_all_by_year(2007)
    preorder_tree = tree.do_preorder_traversal()
    for node in preorder_tree:
        print(node)

    print("==========Printing all devices m.limit of which is gt parameter==========")
    tree.print_all_qt_limit(83)

    print("==========Printing preorder traversal after deleting a tree==========")
    delete_a_tree(tree)
    preorder_tree = tree.do_preorder_traversal()
    for node in preorder_tree:
        print(node)


if __name__ == '__main__':
    main()
