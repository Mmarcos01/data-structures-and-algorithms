from hashtables.hashtable import Hashtable

def hash_tree_intersection(tree1, tree2):
    same_values = []
    tree1 = tree1.pre_order()
    tree2 = tree2.pre_order()
    hashtable = Hashtable()
    for value in tree1:
        hashtable.add(key=str(value), value=value)
    for value in tree2:
        if hashtable.contains(str(value)):
            same_values.append(value)
    return same_values
