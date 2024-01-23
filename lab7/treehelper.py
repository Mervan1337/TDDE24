def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key, left_value, right_value):
    return key + left_value

def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]

def key(tree):
    if is_leaf(tree):
        return tree
    else:
        return tree[1]

