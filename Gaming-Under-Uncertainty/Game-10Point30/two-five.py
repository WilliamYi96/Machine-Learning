import numpy as np 
import sys 
import random
import time
import copy

iteration_times = 10000

pokers = []
for i in range(10):
    pokers += [i+1] * 4
pokers += [0.5] * 14
cur_pokers = copy.deepcopy(pokers)
print(len(pokers))
dealer = [0] * 5
player = [0] * 5
dealer_success = 0
ini_time = time.time()
for i in range(iteration_times):
    # dealer win
    dealer_num, dealer_points = 0, 0
    for j in range(1,6):
        # mrandom = random.randint(0, 53)
        # mrandom = [random.randint(0,53) for _ in range(iteration_times)]
        mrandom = np.random.randint(low=0, high=53, size=iteration_times)
        dealer_num += 1
        cur_pokers.remove(mrandom[i])
        dealer_points += pokers[mrandom[i]]
        if dealer_points > 10.5:
            break
        if j==5 and dealer_points==10.5:
            dealer_success += 1
fin_time = time.time()
print ('Success Rate is {}, running time is {} ms'.format(float(dealer_success)/iteration_times, 1000*(fin_time-ini_time)))
        

