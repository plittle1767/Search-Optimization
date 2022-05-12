"""
    A8 starter code written by David Johnson. All derived works must not
    be posted publicly.

    A8 assignment completed by Preston Little
"""

# Fill in the required assignment functions here.
def curve_scores(one_to_100):
    """
    This function will take a set of mock grade scores and curve the highest to 100. The rest will be added by
    whatever the difference between 100 and the highest score was
    :param one_to_100: a list of scores
    :return: the new curved list
    """
    curved_list = []
    largest_number = 0
    for count in one_to_100:
        next_num = count
        if largest_number < next_num:
            largest_number = next_num
    difference = 100 - largest_number
    for count in one_to_100:
        num = count + difference
        curved_list.append(num)
    return curved_list


def contains_duplicate(string_list):
    """
    This function takes a list and if there are more than one of the same string then it returns True but if there
    aren't any duplicates then it returns False
    :param string_list: a list of string values
    :return: True if the list contains the same string twice or more, otherwise False
    """
    if len(string_list) != len(set(string_list)):
        return True
    else:
        return False


def list_to_string(integer_list):
    """
    Here we're going to turn a list of integers into a list of strings
    :param integer_list: a list of integer values
    :return: a string containing a text representation of the list. The format is the same as if we used print(list)
    and must be exactly
    - start with a [
    - each number except the last one should be followed by a comma and a space. The last number should not have a comma
     and space.
    - end with a ]
    """
    new_list = []
    for element in integer_list:
        new_list.append(str(element))
    return new_list


def lines_from_file(filename):
    """
    This is where we're going to pull out cities.txt file from so we can actually search for a city in the file
    :param filename: a string holding the name of the file to read the lines from
    :return: a new list of string values, where each value is a line from the file
    """
    filename = open(filename, encoding="utf-8")
    lines = filename.readlines()
    return lines


def binary_search_for_matching_string(key, values):
    """
    This function will help activate the text entry box where we will search for a city. It uses a binary search so it
    will cut the list in cities.txt in half each time it searches until it finds the desired city
    :param key: the string to search for
    :param values: a sorted list of strings
    :return: if a string in the list starts with the key string, return the full string from the list. If there is no
    string in the list that starts with the key string, then return None
    """
    lo = 0
    hi = len(values) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if values[mid].startswith(key):
            return values[mid]
        elif values[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    print("Testing curve_scores:")
    print("Expecting a result of [55, 95, 100] and got:", curve_scores([45, 85, 90]))
    print("Expecting a result of [56, 79, 100] and got:", curve_scores([10, 33, 54]))
    print("")
    print("Testing contains_duplicate:")
    print("Expecting a result of False and got:", contains_duplicate(["hi", "bye"]))
    print("Expecting a result of True and got:", contains_duplicate(["the", "boy", "the"]))
    print("")
    print("Testing list_to_string:")
    print("Expecting a result of ['1', '2', '3'] and got:", list_to_string([1, 2, 3]))
    print("Expecting a result of ['1', '2', '4'] and got:", list_to_string([1, 2, 4]))
    print("")
    print("Testing binary_search_for_matching_string with 'b':")
    print("Expecting a result of bear and got:", binary_search_for_matching_string("b", ["ant", "bear", "cat"]))
    print("Testing binary_search_for_matching_string with 'ca':")
    print("Expecting a result of cat and got:", binary_search_for_matching_string("ca", ["ant", "bear", "cat"]))
    print("Testing binary_search_for_matching_string with 'a':")
    print("Expecting a result of ant and got:", binary_search_for_matching_string("a", ["ant", "bear", "cat"]))


if __name__ == "__main__":
    main()
