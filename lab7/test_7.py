import match
import tree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test', choices=["a", "A", "b", "B"], default="", required=False)
args = parser.parse_args()

def matchtester():
    """ Firstly tests the search function then it tests the match function """
    assert match.search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], match.db) == \
        [[['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
        'to', 'computer', 'science']], ['år', 2010]], [['författare', ['john', 'zelle']], 
        ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år', 2009]]]

    assert match.search(['--', ['år', 2042], '--'], match.db) == []

    assert match.search(['--', ['titel', ['&', '&']], '--'], match.db) == \
            [[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]
    


    test_a = [['författare'], ['&', 'Anderstedt']]
    test_db = [['författare'], ['Ludvig', 'Anderstedt']]
    test_b = [['författare'], ['Mervan', 'Palmer']]
    assert match.match(test_db, test_a)
    assert not match.match(test_db, test_b)
    print("The code passed all tests")
    
def treetester():
    """ Tests the functions in tree """

    #-- Tests contains_key function
    assert tree.contains_key(6, [6, 7, 8])
    assert tree.contains_key(2, [6, 7, [[2, 3, 4], 0, []]])
    assert tree.contains_key(69, [23, 12, [15, 420, [1337, 15, [1, 12, [18, 73, 69]]]]])
    assert tree.contains_key(69, [[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],0,[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],69,[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
    assert not tree.contains_key(2, [[], 1, 5])
    
    #-- Tests tree_size function
    assert tree.tree_size([2, 7, []]) == 2
    assert tree.tree_size([]) == 0
    assert tree.tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5
    assert tree.tree_size([[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],0,[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],69,[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]) == 36

    #-- Tests tree_depth function
    assert tree.tree_depth(9) == 1
    assert tree.tree_depth([1, 5, [10, 7, 14]]) ==  3
    assert tree.tree_depth([[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],0,[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],[],[[],69,[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]) == 36

    print("The code passed all tests")


if args.test.upper() == "A":
    matchtester()
elif args.test.upper() == "B":
    treetester()
else:
    matchtester()
    treetester()