import time
from csv import writer
from random import shuffle
from AVLTree import BST
from AVLTree import AVLTree
from itertools import permutations
import matplotlib.pyplot as plt


def countOff(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                cnt += 1
    return cnt



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
    # sorted_arr = tree_max.avl_to_array()
    sorted_arr = tree_max.avl_to_array()
    stop = time.time()
    return stop-start


#myKeys = list(check.keys())
#myKeys.sort()
#check = {i: check[i] for i in myKeys}

# 1234
# 2134
# 2314
# 2341
# Open our existing CSV file in append mode
# Create a file object for this file
N=20
I_NUM = (N*(N-1))//2
point_list=[]
ins_seq = list(range(N))
cnt_x = 0
while cnt_x < 100:
    shuffle(ins_seq)
    x = countOff(ins_seq)
    y = avl_max(ins_seq)
    if x not in [p[0] for p in point_list]:
        point_list.append((x,y))
        cnt_x +=1

point_list.sort()
x_list = [p[0] for p in point_list]
y_list = [p[1] for p in point_list]
print(x_list)
print(y_list)
plt.plot(x_list,y_list)
plt.show()