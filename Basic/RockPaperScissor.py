import random

def play():
    user = input(" R is rock > S is scissors > P is paper\n ")
    computer = random.choice(['r','s','p'])
    print(f'computer is {computer}')
    if user == computer:
        return 'tie'
    if how_to_win(user, computer):
        return 'You win'
    return 'You lost'
    
# function: Condition to Win 
def how_to_win(player, opponent):
    if ( player =='r' and opponent == 's') or (player =='p' and opponent == 'r') \
        or ( player =='s' and opponent == 'p'):
        return True

print(play())