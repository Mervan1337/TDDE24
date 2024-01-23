from typing import Type
from books import *

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        if match(seq[0], pattern[0]):
            return match(seq[1:], pattern[1:])
        else:

            return False
    elif isinstance(pattern[0], list):
        return False
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False

def search(query, db):
    try:
        if isinstance(query, list):
            if isinstance(db, list):
                final = []
                for i in db:
                    if match(i, query):
                        final.append(i)
                return final
            else:
                raise TypeError('DB is not a list')
        else:
            raise TypeError('Query is not a list')
    except TypeError as e:
        raise e
    except NameError as e:
        raise e