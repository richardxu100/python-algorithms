from LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertStart(23)
linkedList.insertStart(35)
linkedList.insertStart(68)

linkedList.traverseList()
print("Num of items %s" % linkedList.size())
print("-------")
linkedList.remove(23)
linkedList.traverseList()
print("Num of items %s" % linkedList.size())
