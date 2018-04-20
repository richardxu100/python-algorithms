from BST import BST

bst = BST()

bst.insert(13)
# print(bst.getMin())
bst.insert(12)
# print(bst.getMin())
bst.insert(100)
bst.insert(103)
bst.traverseInOrder()
bst.remove(13)

print("-----------------")
# print(bst.getMax())
print("Size %s" % bst.getSize())

bst.traverseInOrder()
# print("BST root %s" % bst.getRoot().data)
# print("BST root leftChild %s" % bst.getRoot().leftChild.data)
# print("BST root rightChild %s" % bst.getRoot().rightChild.data)
# print(bst.getMin())

# bst.traverseInOrder()
