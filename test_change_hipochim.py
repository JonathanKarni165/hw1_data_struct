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
'''
while len(check) < 10:
    lst = list(range(10))
    shuffle(lst)
    num = countOff(lst)
    if len(set(range(num-9, num+10)).intersection(set(check.keys()))) == 0:
        check[num] = lst

print(check)
'''

def flip_series(lst):
    yield lst
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            tmp = lst[j+1]
            lst[j+1] = lst[j]
            lst[j] = tmp
            yield lst
    

def avl_max(lst):
    tree_max = AVLTree()

    start = time.time()
    total_rotation_num = 0
    for n in lst:
        total_rotation_num +=tree_max.insert(n,f'{n}','max')
    sorted_arr = tree_max.avl_to_array()

    stop = time.time()
    return total_rotation_num


#myKeys = list(check.keys())
#myKeys.sort()
#check = {i: check[i] for i in myKeys}

# 1234
# 2134
# 2314
# 2341
# Open our existing CSV file in append mode
# Create a file object for this file
N=100
I_NUM = (N*(N-1))//2
print(avl_max([list(range(15))]))
with open('exp1.csv', 'a') as exp_file:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(exp_file)

    gen1 = flip_series(list(range(N)))
    gen2 = flip_series([0,1,3,2] + list(range(4,N)))
    gen3 = flip_series([0,1,2,4,3] + list(range(5,N)))
    # {(I=5 : (65, 8)}
    dict_I = {key:[0,0] for key in range(0,I_NUM+1)}
    for (g1,g2,g3) in zip(gen1,gen2,gen3):
        print(g1,'\n\n',g2,'\n\n',g3,'\n\n')
        dict_I[countOff(g1)][0]+=1
        dict_I[countOff(g1)][1]+=avl_max(g1)

        dict_I[countOff(g2)][0]+=1
        dict_I[countOff(g2)][1]+=avl_max(g2)

        dict_I[countOff(g3)][0]+=1
        dict_I[countOff(g3)][1]+=avl_max(g2)
    for i in range(len(dict_I)):
        writer_object.writerow([i,dict_I[i][1]/dict_I[i][0]])

    
    
    # Close the file object
    exp_file.close()

