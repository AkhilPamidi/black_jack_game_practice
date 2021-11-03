from art import logo
print(logo)
import random
print("welcome to the black jack game project")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
  return random.choice(cards)
computer_cards=[]
user_cards=[]
#for the sake of user cards
for card in range(2):
  user_cards.append(deal_card())
for card in range(1):
  computer_cards.append(deal_card())
print(f"user cards: {user_cards}\ncomputer cards:{computer_cards}")
#rules for the game to check
def check_cards(player_cards):
        if sum(player_cards)>21:
            while 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
        while sum(player_cards)<=17:
            player_cards.append(deal_card())

def declare_winner(player1,player2):
    if sum(player1)>sum(player2):
        print(f"user_cards:{player1},computer_cards:{player2}")
        print(f"user won the game")
    elif sum(player2)>sum(player1):
        print(f"computer_cards:{player2},user_cards:{player1}")
        print(f"you loose the game")

game_on=True
while game_on:
    if input("if you want to take another card type 'y' if you don't want type 'n'").lower()=="y":
        user_cards.append(deal_card())
        print(user_cards)
    else:
        check_cards(user_cards)
        check_cards(computer_cards)
        declare_winner(user_cards,computer_cards)
        if input("type 'y' to play again type 'n' to stop the game ").lower()=='y':
            game_on=True
        else:
            game_on=False




