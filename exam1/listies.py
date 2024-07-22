
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    return lst[:-1]
    #pass  # implement me

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    return lst[2:-1]
    #pass  # implement me

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    return [a] + lst
    pass  # implement me

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    return lst + [a]
    #pass  # implement me

def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    return lst[2:]
    #pass  # implement me

def drop_last_two(lst):
    """
    This function takes a list and returns a list with the last two items removed.
    """
    return lst[:-2]

    #pass  # implement me

