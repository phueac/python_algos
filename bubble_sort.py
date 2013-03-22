def bubble_sort(l):
    '''Sorts a Python list of numbers into ascending order'''

    if len(l) == 1:
        return l

    npairs = len(l) - 1

    for j in range(npairs):
        for i in range(npairs):
            if (l[i] > l[i+1]):
                tmp = l[i+1]
                l[i+1] = l[i]
                l[i] = tmp
    
    return l
