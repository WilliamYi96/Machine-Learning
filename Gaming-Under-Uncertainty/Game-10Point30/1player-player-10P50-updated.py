import numpy as np 
import sys 
import random
import time
import copy

iteration_times = 10000
check_times = 50

pokers = []
for i in range(10):
    pokers += [i+1] * 4
pokers += [0.5] * 14

dealer = [0] * 5
player = [0] * 5
dealer_success = 0
ini_time = time.time()
success_rate_cal = 0

for j in range(check_times):
    for i in range(iteration_times):
        cur_pokers = copy.deepcopy(pokers)
        dealer_points, player_points = 0, 0
        # dealer init with a poker
        rand_dealer = random.randint(0, len(cur_pokers)-1)
        dealer_points += cur_pokers[rand_dealer]
        cur_pokers.remove(cur_pokers[rand_dealer])
        # player init with a poker
        rand_player = random.randint(0, len(cur_pokers)-1)
        player_points += cur_pokers[rand_player]
        cur_pokers.remove(cur_pokers[rand_player])
        # print(rand_dealer, rand_player)

        # dealer win
        for j in range(1, 5):
            # print(len(cur_pokers))
            mrandom = random.randint(0, len(cur_pokers)-1)
            # print('mrandom is {}'.format(mrandom))
            dealer_points += cur_pokers[mrandom]
            cur_pokers.remove(cur_pokers[mrandom])

            if dealer_points > 10.5:
                break
            if j==4 and dealer_points==10.5:
                dealer_success += 1
    success_rate_cal += float(dealer_success)/iteration_times
    print ('Success Rate is {}'.format(float(dealer_success)/iteration_times))

fin_time = time.time()
avg_rate = float(dealer_success)/iteration_times/check_times
print ('Average Success Rate is {}'.format(avg_rate))
print ('Running time is {} ms'.format(1000*(fin_time-ini_time)))
        

