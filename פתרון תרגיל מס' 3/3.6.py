# Helper to check if any list inside the main list is empty
def has_empty(lsts):
    if not lsts:
        return False
    if not lsts[0]:
        return True
    return has_empty(lsts[1:])

# Sorts each inner list (Tail Recursion)
def sort_lists_tail(lists, acc=None):
    if acc is None: acc = []
    if not lists:
        return acc
    return sort_lists_tail(lists[1:], acc + [sorted(lists[0])])

# Gets the first element of each inner list (Tail Recursion)
def get_firsts_tail(lsts, acc=()):
    if not lsts:
        return acc
    return get_firsts_tail(lsts[1:], acc + (lsts[0][0],))

# Gets the rest of the elements of each inner list (Tail Recursion)
def get_rests_tail(lsts, acc=None):
    if acc is None: acc = []
    if not lsts:
        return acc
    return get_rests_tail(lsts[1:], acc + [lsts[0][1:]])

# Core recursive zip logic (Tail Recursion)
def recursive_zip_tail(lists, acc=None):
    if acc is None: acc = []
    if not lists or has_empty(lists):
        return acc
    firsts = get_firsts_tail(lists)
    rests = get_rests_tail(lists)
    return recursive_zip_tail(rests, acc + [firsts])

def sortedzip(lists):
    sorted_lists = sort_lists_tail(lists)
    return recursive_zip_tail(sorted_lists)

print(list(sortedzip([[3,1,2], [5,6,4], ['a','b','c']])))