from treehelper import *


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """ 
    Checks firstly if a tree is empty, 
    if not it checks if it is a leaf, if it is a leaf it return the leafs value squared e.g. if a leaf is valued two then: 2^2 = 4
    if not we can assume it is still in a branch and we repeat recursive
    """
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):
        return leaf_fn(key(tree))
    else:
        return inner_node_fn(
            key(tree), 
            traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn), 
            traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        )

def contains_key(x, tree):
    """ Checks if a specific key is in tree """
    def leaf_fn(tree):
        return key(tree) == x
    def inner_node_fn(key, left_value, right_value):
        return left_value or right_value or x == key
    def empty_tree_fn():
        return False
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_size(tree):
    """ Checks size of a tree """
    def leaf_fn(tree):
        return 1
    def inner_node_fn(key, left_value, right_value):
        return 1 + left_value + right_value
    def empty_tree_fn():
        return 0
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_depth(tree):
    """ Checks depth of a tree """
    def leaf_fn(tree):
        return 1
    def inner_node_fn(key, left_value, right_value):
        if right_value > left_value:
            return 1 + right_value
        else:
            return 1 + left_value
    def empty_tree_fn():
        return 0
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)
