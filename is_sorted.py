def is_sorted(lst):
    """Takes a list and returns True if the list is sorted and False otherwise"""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


lst1 = [1, 2, 5, 6, 9]
print(is_sorted(lst1))
