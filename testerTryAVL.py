import time
from csv import writer
from random import shuffle
from AVLTree import BST
from AVLTree import AVLTree



#####################################
# experiment 1- sort with bst from max
def bst_root_sorted(n):
    insert_seq1 = [i for i in range(n)]
    start = time.time()

    tree_sort_root = BST()

    # create tree from max
    for i in range(len(insert_seq1)):
        tree_sort_root.insert_naive(insert_seq1[i], str(i))
    
    sorted_arr = tree_sort_root.avl_to_array()
    stop = time.time()
    # print(sorted_arr)

    return stop - start


#####################################
# experiment 1- sort with bst from max

def bst_max_sorted(n):
    insert_seq1 = [i for i in range(n)]
    start = time.time()

    tree_sort_max = BST()

    for i in range(len(insert_seq1)):
        tree_sort_max.insert_naive(insert_seq1[i], str(i),'max')

    sorted_arr = tree_sort_max.avl_to_array()
    

    stop = time.time()
    # print(sorted_arr)
    
    return stop-start




def bst_root_reverse(n):
    insert_seq2 = [i for i in range(n)][::-1]
        
    start = time.time()
    tree_unsort_root = BST()

    for i in range(len(insert_seq2)):
        tree_unsort_root.insert_naive(insert_seq2[i], str(i))
    
    sorted_arr = tree_unsort_root.avl_to_array()
    stop = time.time()
    # print(sorted_arr)
    return stop - start



def bst_max_reverse(n):
    insert_seq2 = [i for i in range(n)][::-1]
    start = time.time()

    tree_unsort_max = BST()

    for i in range(len(insert_seq2)):
        tree_unsort_max.insert_naive(insert_seq2[i], str(i),'max')
    
    
    sorted_arr = tree_unsort_max.avl_to_array()
    stop = time.time()
    # print(sorted_arr)
    return stop-start


# avlllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def avl_root_sorted(n):
    insert_seq1 = [i for i in range(n)]
    start = time.time()

    tree_sort_root = AVLTree()

    # create tree from max
    for i in range(len(insert_seq1)):
        tree_sort_root.insert(insert_seq1[i], str(i))
    
    sorted_arr = tree_sort_root.avl_to_array()
    stop = time.time()
    # print(sorted_arr)
    return stop - start


#####################################
# experiment 1- sort with bst from max

def avl_max_sorted(n):
    insert_seq1 = [i for i in range(n)]
    start = time.time()

    tree_sort_max = AVLTree()

    for i in range(len(insert_seq1)):
        tree_sort_max.insert(insert_seq1[i], str(i),'max')
    
    sorted_arr = tree_sort_max.avl_to_array()
    stop = time.time()
    # print(sorted_arr)
    return stop-start




def avl_root_reverse(n):
    insert_seq2 = [i for i in range(n)][::-1]
    start = time.time()
    tree_unsort_root = AVLTree()

    for i in range(len(insert_seq2)):
        tree_unsort_root.insert(insert_seq2[i], str(i))
    
    sorted_arr = tree_unsort_root.avl_to_array()
    stop = time.time()
    # print(sorted_arr)
    return stop - start



def avl_max_reverse(n):
    insert_seq2 = [i for i in range(n)][::-1]
    start = time.time()

    tree_unsort_max = AVLTree()

    for i in range(len(insert_seq2)):
        tree_unsort_max.insert(insert_seq2[i], str(i),'max')
    sorted_arr = tree_unsort_max.avl_to_array() 
    stop = time.time()
    # print(sorted_arr)
    return stop-start




# Open our existing CSV file in append mode
# Create a file object for this file
with open('exp.csv', 'a') as exp_file:

    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(exp_file)

    # Pass the list as an argument into
    # the writerow()
    # writer_object.writerow(List)

    lst = [100, 500, 2500, 5000, 10000, 15000]
    for n in range(len(lst)):
        print("start " + str(lst[n]))
        row = [0 for i in range(8)]
        func_lst = [bst_root_sorted, bst_max_sorted, bst_root_reverse, bst_max_reverse, avl_root_sorted, avl_max_sorted, avl_root_reverse, avl_max_reverse]
        for i in range(8):
            row[i] = round(func_lst[i](lst[n]), 10)
        writer_object.writerow(row)
    # Close the file object
    exp_file.close()
    print("finished")