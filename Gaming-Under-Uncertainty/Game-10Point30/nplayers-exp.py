import numpy as np 
import random
import time
import copy

iteration_times = 10000
check_times = 5
players_num = 5 # num <= 9

pokers = []
for i in range(10):
    pokers += [i+1] * 4
pokers += [0.5] * 14

player_success = 0
ini_time = time.time()
success_rate_cal = 0
dealer_exp_cal, player_exp_cal = 0, [0]*players_num
dealer_decision_point = 7.0
player_decision_point = 7.5
avg_player_exp = [0]*players_num

for j in range(check_times):
    dealer_win, player_win = 0, [0]*players_num
    dealer_exp, player_exp = 0, [0]*players_num
    
    for i in range(iteration_times):
        dealer_definite_win = False
        player_definite_win = [False]*players_num

        cur_pokers = copy.deepcopy(pokers)
        dealer_points, player_points = 0, [0]*players_num

        # dealer init with a poker
        rand_dealer = random.randint(0, len(cur_pokers)-1)
        dealer_points += pokers[rand_dealer]
        cur_pokers.remove(pokers[rand_dealer])
        # players init with a poker
        for m in range(players_num):
            rand_player = random.randint(0, len(cur_pokers)-1)
            # print(len(cur_pokers), rand_player)
            player_points[m] += pokers[rand_player]
            cur_pokers.remove(cur_pokers[rand_player])
            # del cur_pokers[rand_dealer]

        # dealer round
        for j in range(1, 5):
            if j==4 and dealer_points==10.5:
                dealer_definite_win = True
                dealer_exp += 2*players_num
                for m in range(players_num):  
                    player_exp[m] -= 2
            elif j==4 or dealer_points==10.5:
                dealer_definite_win = True
                dealer_exp += 1*players_num
                for m in range(players_num):  
                    player_exp[m] -= 1
            if dealer_points >= dealer_decision_point:
                break

            mrandom = random.randint(0, len(cur_pokers)-1)
            dealer_points += cur_pokers[mrandom]
            cur_pokers.remove(cur_pokers[mrandom])

        # player round
        if not dealer_definite_win:
            for m in range(players_num):
                for k in range(1, 5):
                    if player_points[m] >= 10.5:
                        dealer_definite_win = True
                        dealer_exp += 1
                        player_exp[m] -= 1
                        break
                    elif player_points[m]==10.5 and k==4:
                        player_definite_win[m] = True
                        player_exp[m] += 4
                        dealer_exp -= 4
                    elif player_points[m]==10.5 or k==4:
                        player_definite_win[m] = True
                        player_exp[m] += 2
                        dealer_exp -= 2

                    if player_points[m] >= player_decision_point:
                        break

                    mrandom = random.randint(0, len(cur_pokers)-1)
                    player_points[m] += cur_pokers[mrandom]
                    cur_pokers.remove(cur_pokers[mrandom])

        # print(dealer_points, player_points)
        # judge winner
        if dealer_definite_win:
            dealer_win += 1
        else:
            for m in range(players_num):  
                if player_definite_win[m]:
                    player_win[m] += 1
                else:
                    if player_points[m] > 10.5:
                        dealer_win += 1
                        dealer_exp += 1
                        player_exp[m] -= 1
                    elif dealer_points > 10.5 and player_points[m] < 10.5:
                        player_win[m] += 1
                        player_exp[m] += 1
                        dealer_exp -= 1
                    elif dealer_points < 10.5 and player_points[m] < 10.5:
                        if dealer_points >= player_points[m]:
                            dealer_win += 1
                            dealer_exp += 1
                            player_exp[m] -= 1
                        else:
                            player_win[m] += 1
                            player_exp[m] += 1
                            dealer_exp -= 1

    success_rate_cal += float(dealer_win)/iteration_times
    dealer_exp_cal += float(dealer_exp)/iteration_times
    print ('Success Rate is {}'.format(float(dealer_win)/iteration_times))
    for m in range(players_num):
        player_exp_cal[m] += float(player_exp[m])/iteration_times
        print ('Dealer Exp: {}, Player {} Exp: {}'.format(
            dealer_exp_cal, m+1, player_exp_cal[m]
        ))

fin_time = time.time()
avg_rate = success_rate_cal/check_times
avg_dealer_exp = dealer_exp_cal/check_times
print ('Average Success Rate is {}'.format(avg_rate))
print ('Average Dealer Exp is {}'.format(avg_dealer_exp))
for m in range(players_num):
    avg_player_exp[m] = player_exp_cal[m]/check_times
    print ('Average Player Exp is {}'.format(avg_player_exp[m]))
print ('Running time is {} s'.format(fin_time-ini_time))