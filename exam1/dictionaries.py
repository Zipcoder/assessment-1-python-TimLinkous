
def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        datadict.pop(key, None)
    return datadict
    #pass

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()
    
    # if key in datadict:
    #     return True
    # elif key not in datadict:
    #     return False
    #pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key = ddd.get)
    #pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key = ddd.get)
    #pass

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    freq = []
    for i in word:
        letter_count = word.count(i)
        freq.append((i, letter_count))
    result = dict(freq)
    return result
    #pass