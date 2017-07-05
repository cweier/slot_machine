from random import randint




def play(stake):
    while question(stake) == True:
        print("Let's Spin!")
        print("You currently have $" + str(stake))
        reel1 = spin_result()
        reel2 = spin_result()
        reel3 = spin_result()
        print(reel1 + " " + reel2 + " " + reel3)
        payout_total = payout(reel1, reel2, reel3)
        if payout_total > 0:
            print("You won $" + str(payout_total) + " on that spin!")
        stake += payout_total
        print('Now you have $' + str(stake))

def question(stake):
    answer = input("Would you like to spin? ")
    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        print("You are leaving with $" + str(stake))
        return False
    else:
        print("no valid, try again")
        play(stake)

def spin_result():
    outcomes = ['CHERRY', 'BAR', 'ORANGE', 'LEMON', 'DAIMOND', 'SEVEN']
    return outcomes[spin()]

def spin():
    return randint(0, 5)

def payout(reel1, reel2, reel3):
    if reel1 == 'CHERRY' and reel2 == 'CHERRY' and reel3 == 'CHERRY':
        return 200
    elif reel1 == 'ORANGE' and reel2 == 'ORANGE' and reel3 == 'ORANGE':
        return 150
    else:
        return -1


play(50)



# from time import sleep
#
#
#
# credits = 100
# jackpot = 1000
# # spins = 1
# # while credits > 0:
# #     jackpot += 2
# #     spins += 1
# #     reel_one = randint(1, 100)
# #     reel_two = randint(1, 100)
# #     reel_three = randint(1, 100)
# #     if reel_one == 100 and reel_two == 100 and reel_three == 100:
# #         print("You won the jackpot of " + str(jackpot))
# #         print("It took " + str(spins) + " to win the jackpot.")
# #         break
# #
# #
#
#
#
#
#
#
# while credits > 0:
#     jackpot += 1
#     credits -= 1
#     print(jackpot)
#     reel_one = randint(1,100)
#     if reel_one >= 1 and reel_one < 20:
#         print("Blank")
#     elif reel_one >= 20 and reel_one < 55:
#         print("Orange")
#     elif reel_one >= 55 and reel_one < 70:
#         print("Cherry")
#     elif reel_one >= 70 and reel_one < 80:
#         print("Daimond")
#     elif reel_one >= 80 and reel_one < 100:
#         print("BAR")
#     elif reel_one == 100:
#         print(7)
#     sleep(1)
#
#     reel_two = randint(1,100)
#     if reel_two >= 1 and reel_two < 20:
#         print("Blank")
#     elif reel_two >= 20 and reel_two < 55:
#         print("Orange")
#     elif reel_two >= 55 and reel_two < 70:
#         print("Cherry")
#     elif reel_two >= 70 and reel_two < 80:
#         print("Daimond")
#     elif reel_two >= 80 and reel_two < 100:
#         print("BAR")
#     elif reel_two == 100:
#         print(7)
#     sleep(1)
#
#     reel_three = randint(1,100)
#     if reel_three >= 1 and reel_three < 20:
#         print("Blank")
#     elif reel_three >= 20 and reel_three < 55:
#         print("Orange")
#     elif reel_three >= 55 and reel_three < 70:
#         print("Cherry")
#     elif reel_three >= 70 and reel_three < 80:
#         print("Daimond")
#     elif reel_three >= 80 and reel_three < 100:
#         print("BAR")
#     elif reel_three == 100:
#         print(7)
#     sleep(1)
#
#     if reel_one == reel_two and reel_two == reel_three:
#         if reel_one == "Orange":
#             credits += 3
#         if reel_one == "Cherry":
#             credits += 5
#         if reel_one == "Daimond":
#             credits += 15
#         if reel_one == "BAR":
#             credits += 5
#         if reel_one == 7:
#             credits += jackpot
#     else:
#         print("No wins")
#         print(credits)