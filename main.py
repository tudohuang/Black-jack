import random
import math
player_money = 100000
def get_card():
  card = math.ceil(random.random() * 13)
  return card

def sum_cards(cards):
  sum = 0
  for card in cards:
    if card > 10:
      card = 10
    sum = sum + card
    #print(sum)
    
  return sum

play = True

while play:
  print('Player money:', player_money)
  bet = input('Game Start !! Place your bet: ')
  bet = int(bet)
  card1 = get_card()
  card2 = get_card()
  cards = [card1, card2]

  print('Your cards are:', cards)
  print('The sum of cards is ', sum_cards(cards))

  card1 = get_card()
  card2 = get_card()
  cards_b = [card1, card2]

  print("Banker's card is:", cards_b[0])
  #print('The sum of cards is ', sum_cards(cards_b))

  want = True
  boom = False

  while want:

    YN = input('Do you want to add a card (Y/N)?')
    YN = YN.lower()
    if YN == 'y':
      want = True
    else:
      want = False

    print(want)

    if want:
      cards.append(get_card())
      print('Your cards are:', cards)
      print('The sum of cards is ', sum_cards(cards))
      if sum_cards(cards)>21:
        boom = True
        print('boom!')
        print('You lost your bet:', bet)
        want = False
        player_money = player_money - bet
        print('Player money:', player_money)

  if not boom:
    print("Banker's cards are:", cards_b)
    print('The sum is:',sum_cards(cards_b))

    while sum_cards(cards_b)<16:
      cards_b.append(get_card())
      print('Banker cards are:', cards_b)
      print('The sum of cards is ', sum_cards(cards_b))


    print('The final banker cards are:', cards_b)
    print('The final sum of banker cards is ', sum_cards(cards_b))

    if (sum_cards(cards_b) > 21) or (sum_cards(cards) > sum_cards(cards_b)):
      print('Player won!')
      player_money = player_money + bet

    elif sum_cards(cards) == sum_cards(cards_b):
      print('Push !')
    else:
      print('Player lost!')
      player_money = player_money - bet


    print('Player money:', player_money)
  if player_money < 0:
    print("Bankrupt!!")
    play = False 
    
  YN = input('Do you want to play again(Y/N)?')
  YN = YN.lower()
  if YN == 'y' and player_money >= 0:
    play = True
  else:
    play = False
  

    
