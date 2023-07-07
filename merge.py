def merge(list1, list2):
    """ Takes two already sorted lists of possibly different lengths and merges them into a single sorted list"""
    p1, p2 = 0, 0
    new_list = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            new_list.append(list1[p1])
            p1 += 1
        else:
            new_list.append(list2[p2])
            p2 += 1

    if p1 == len(list1):
        new_list.extend(list2[p2:])
    else:
        new_list.extend(list1[p1:])
    return new_list


l1 = [1, 2, 6, 8, 9, 12, 15, 19]
l2 = [3, 4, 5, 7, 25, 26, 28]
print(merge(l1, l2))



