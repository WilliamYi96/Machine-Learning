import numpy as np 
import random
import time
import copy

iteration_times = 10000
check_times = 50

pokers = []
for i in range(10):
    pokers += [i+1] * 4
pokers += [0.5] * 14

player_success = 0
ini_time = time.time()
success_rate_cal = 0
dealer_decision_point = 7.0

for j in range(check_times):
    for i in range(iteration_times):
        Flag = True

        cur_pokers = copy.deepcopy(pokers)
        dealer_points, player_points = 0, 0

        # dealer init with a poker
        rand_dealer = random.randint(0, len(cur_pokers)-1)
        cur_pokers.remove(pokers[rand_dealer])
        # player init with a poker
        rand_player = random.randint(0, len(cur_pokers)-1)
        cur_pokers.remove(pokers[rand_dealer])

        # dealer not win first
        dealer_num, dealer_points = 0, 0
        for j in range(1, 5):
            if j==4 or dealer_points==10.5:
                Flag = False
                break
            if dealer_points >= dealer_decision_point:
                break

            mrandom = random.randint(0, len(cur_pokers)-1)
            dealer_points += cur_pokers[mrandom]
            cur_pokers.remove(cur_pokers[mrandom])
        
        if Flag:
            for k in range(1, 5):
                if player_points > 10.5:
                    break
                if k==4 and player_points==10.5:
                    player_success += 1

                mrandom = random.randint(0, len(cur_pokers)-1)
                player_points += cur_pokers[mrandom]
                cur_pokers.remove(cur_pokers[mrandom])


    success_rate_cal += float(player_success)/iteration_times
    print ('Success Rate is {}'.format(float(player_success)/iteration_times))

fin_time = time.time()
avg_rate = float(player_success)/iteration_times/check_times
print ('Average Success Rate is {}'.format(avg_rate))
print ('Running time is {} s'.format((fin_time-ini_time)))