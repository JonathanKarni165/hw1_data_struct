import time
from csv import writer
from random import shuffle
from AVLTree import BST
from AVLTree import AVLTree

from itertools import permutations


def countOff(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                cnt += 1
    return cnt


#####################################
# experiment 1- sort with bst from max
def bst_root_sorted(lst):

    start = time.time()

    tree_sort_root = BST()

    # create tree from max
    for i in range(len(lst)):
        tree_sort_root.insert_naive(lst, str(i))

    sorted_arr = tree_sort_root.avl_to_array()
    stop = time.time()
    print(sorted_arr)

    return stop - start


#####################################
# experiment 1- sort with bst from max

def bst_max_sorted(lst):

    start = time.time()

    tree_sort_max = BST()

    for i in range(len(lst)):
        tree_sort_max.insert_naive(lst, str(i), 'max')

    sorted_arr = tree_sort_max.avl_to_array()

    stop = time.time()
    print(sorted_arr)

    return stop - start


def bst_root_reverse(lst):


    start = time.time()
    tree_unsort_root = BST()

    for i in range(len(lst)):
        tree_unsort_root.insert_naive(lst[i], str(i))

    sorted_arr = tree_unsort_root.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return stop - start


def bst_max_reverse(lst):

    start = time.time()

    tree_unsort_max = BST()

    for i in range(len(lst)):
        tree_unsort_max.insert_naive(lst[i], str(i), 'max')

    sorted_arr = tree_unsort_max.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return stop - start


# avlllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def avl_root_sorted(lst):

    start = time.time()

    tree_sort_root = AVLTree()

    # create tree from max
    for i in range(len(lst)):
        tree_sort_root.insert(lst[i], str(i))

    sorted_arr = tree_sort_root.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return stop - start


#####################################
# experiment 1- sort with bst from max

def avl_max_sorted(lst):

    start = time.time()

    tree_sort_max = AVLTree()

    for i in range(len(lst)):
        tree_sort_max.insert(lst[i], str(i), 'max')

    sorted_arr = tree_sort_max.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return (stop - start)*(10**6)


def avl_root_reverse(lst):

    start = time.time()
    tree_unsort_root = AVLTree()

    for i in range(len(lst)):
        tree_unsort_root.insert(lst[i], str(i))

    sorted_arr = tree_unsort_root.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return stop - start


def avl_max_reverse(lst):

    start = time.time()

    tree_unsort_max = AVLTree()

    for i in range(len(lst)):
        tree_unsort_max.insert(lst[i], str(i), 'max')
    sorted_arr = tree_unsort_max.avl_to_array()
    stop = time.time()
    print(sorted_arr)
    return stop - start





check = {}

# l = list(permutations(range(10)))
# for i in range(len(l)):
#     a = countOff(l[i])
#     if a % 5 == 0 and len(set(range(a-4, a+5)).intersection(set(check.keys()))) == 0:
#         check[a] = l[i]
#         print(a)
#

while len(check) < 40:
    lst = list(range(60))
    shuffle(lst)
    num = countOff(lst)
    if len(set(range(num-9, num+10)).intersection(set(check.keys()))) == 0:
        check[num] = lst
        print(num)


myKeys = list(check.keys())
myKeys.sort()
check = {i: check[i] for i in myKeys}

# Open our existing CSV file in append mode
# Create a file object for this file
with open('exp1.csv', 'a') as exp_file:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(exp_file)

    # Pass the list as an argument into
    # the writerow()
    # writer_object.writerow(List)
    for n in range(len(check)):
        row = [0 for i in range(2)]
        func_lst = [avl_max_sorted]
        row[0] = list(check.keys())[n]
        row[1] = round(func_lst[0](check[list(check.keys())[n]]), 10)
        writer_object.writerow(row)
    # Close the file object
    exp_file.close()

