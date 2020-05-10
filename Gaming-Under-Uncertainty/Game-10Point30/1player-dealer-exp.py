import numpy as np 
import random
import time
import copy

iteration_times = 10000
check_times = 5

pokers = []
for i in range(10):
    pokers += [i+1] * 4
pokers += [0.5] * 14

player_success = 0
ini_time = time.time()
success_rate_cal = 0
dealer_exp_cal, player_exp_cal = 0, 0
dealer_decision_point = 7.0
player_decision_point = 7.5

for j in range(check_times):
    dealer_win, player_win = 0, 0
    dealer_exp, player_exp = 0, 0
    
    for i in range(iteration_times):
        dealer_definite_win = False
        player_definite_win = False

        Flag = True

        cur_pokers = copy.deepcopy(pokers)
        dealer_points, player_points = 0, 0

        # dealer init with a poker
        rand_dealer = random.randint(0, len(cur_pokers)-1)
        dealer_points += pokers[rand_dealer]
        cur_pokers.remove(pokers[rand_dealer])
        # player init with a poker
        rand_player = random.randint(0, len(cur_pokers)-1)
        player_points += pokers[rand_player]
        cur_pokers.remove(pokers[rand_player])

        # dealer round
        for j in range(1, 5):
            # print("dealer point is {}".format(dealer_points))
            # if j==4 or dealer_points==10.5:
            #     dealer_definite_win = True
            #     break
            if j==4 and dealer_points==10.5:
                dealer_definite_win = True
                dealer_exp += 2
            elif j==4 or dealer_points==10.5:
                dealer_definite_win = True
                dealer_exp += 1
            if dealer_points >= dealer_decision_point:
                break

            mrandom = random.randint(0, len(cur_pokers)-1)
            dealer_points += cur_pokers[mrandom]
            cur_pokers.remove(cur_pokers[mrandom])
        
        # player round
        if not dealer_definite_win:
            for k in range(1, 5):
                # print("player point is {}".format(player_points))
                if player_points >= 10.5:
                    dealer_definite_win = True
                    dealer_exp += 1
                    break
                # if player_points <= 10.5 and k==4:
                #     player_definite_win = True
                #     break
                elif player_points==10.5 and k==4:
                    player_definite_win = True
                    player_exp += 4
                elif player_points==10.5 or k==4:
                    player_definite_win = True
                    player_exp += 2
                
                if player_points >= player_decision_point:
                    break
                
                mrandom = random.randint(0, len(cur_pokers)-1)
                player_points += cur_pokers[mrandom]
                cur_pokers.remove(cur_pokers[mrandom])

        # print(dealer_points, player_points)
        # judge winner
        if dealer_definite_win:
            dealer_win += 1
        elif player_definite_win:
            player_win += 1
        else:
            if player_points > 10.5:
                dealer_win += 1
                deal_exp += 1
            elif dealer_points > 10.5 and player_points < 10.5:
                player_win += 1
                player_exp += 1
            elif dealer_points < 10.5 and player_points < 10.5:
                if dealer_points >= player_points:
                    dealer_win += 1
                    dealer_exp += 1
                else:
                    player_win += 1
                    player_exp += 1

    success_rate_cal += float(dealer_win)/iteration_times
    dealer_exp_cal += float(dealer_exp)/iteration_times
    player_exp_cal += float(player_exp)/iteration_times
    print ('Success Rate is {}'.format(float(dealer_win)/iteration_times))
    print ('Dealer Exp: {}, Player Exp: {}'.format(
        dealer_exp_cal, player_exp_cal
    ))

fin_time = time.time()
avg_rate = success_rate_cal/check_times
avg_dealer_exp = dealer_exp_cal/check_times
avg_player_exp = player_exp_cal/check_times
print ('Average Success Rate is {}'.format(avg_rate))
print ('Average Dealer Exp is {}'.format(avg_dealer_exp))
print ('Average Player Exp is {}'.format(avg_player_exp))
print ('Running time is {} ms'.format(1000*(fin_time-ini_time)))