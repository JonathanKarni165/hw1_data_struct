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
x=[]
y=[]
print(avl_max([list(range(15))]))


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
    x.append(i)
    y.append(dict_I[i][1]/dict_I[i][0])


plt.plot(x,y)
plt.show()