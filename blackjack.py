import random
import math
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# 初始玩家金錢
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
    return sum



game_status = {
    "start_game" : False,
    "bet": 0,
    "cards": [],
    "cards_b": [],
    "want": True,
    "boom": False,
}


def add_card():
    global player_money
    game_status["cards"].append(get_card())
    # 檢查是否爆牌
    if game_status["start_game"] == True:
        if sum_cards(game_status["cards"]) > 21 :
            game_status["boom"] = True
            player_money -= game_status["bet"]
            status_label.config(text=f'Boom! You lost your bet: {game_status["bet"]}\nPlayer money: {player_money}')
        else:
            money_label.config(text=f'Your cards are: {game_status["cards"]}\nThe sum of cards is {sum_cards(game_status["cards"])}')
    else:
        status_label.config(text='error')


def start_game():
    global player_money
    bet = int(bet_entry.get())
    # 遊戲狀態更新
    if bet <= player_money:
        game_status["bet"] = bet
        game_status["cards"] = [get_card(), get_card()]
        game_status["cards_b"] = [get_card(), get_card()]
        game_status["want"] = True
        game_status["boom"] = False
        game_status["start_game"] = True
        # 更新狀態標籤
        money_label.config(text=f'Your cards are: {game_status["cards"]}\nBanker\'s card is: {game_status["cards_b"][0]}\nThe sum of cards is {sum_cards(game_status["cards"])}')
    else:
        money_label.config(text=f"You don't have this much money!\n You just have ${player_money}")



def stop_game():
    global player_money
    if not game_status["boom"]:
        while sum_cards(game_status["cards_b"]) < 16:
            game_status["cards_b"].append(get_card())
        if (sum_cards(game_status["cards_b"]) > 21) or (sum_cards(game_status["cards"]) > sum_cards(game_status["cards_b"])):
            player_money += game_status["bet"]
            result = 'Player won!'
        elif sum_cards(game_status["cards"]) == sum_cards(game_status["cards_b"]):
            result = 'Push !'
        else:
            player_money -= game_status["bet"]
            result = 'Player lost!'
        status_label.config(text=f'The final banker cards are: {game_status["cards_b"]}\nThe final sum of banker cards is {sum_cards(game_status["cards_b"])}\n{result}\nPlayer money: {player_money}')
# 創建視窗
root = ThemedTk(theme="classic")
root.title("🎲Black Jack🎲")
root.geometry("700x500")
root.configure(bg="#F9FBE7")

title_label = ttk.Label(root, text="🎲Black Jack🎲", font=("Helvetica", 32, "bold"), background="#F9FBE7", foreground="#008C95")
title_label.pack(pady=10)

money_label = ttk.Label(root, text=f'You have ${player_money}',font=("Helvetica", 20, "bold"), background="#F9FBE7")
money_label.pack(pady=10)


status_label = ttk.Label(root, text="",font=("Helvetica", 20, "bold"), background="#F9FBE7", foreground="#008C95")
status_label.pack(pady=10)

bet_entry = ttk.Entry(root)
bet_entry.pack()


start_button = ttk.Button(root, text="Start Game", command=start_game)
start_button.pack()

add_card_button = ttk.Button(root, text="Add Card", command=add_card)
add_card_button.pack()

stop_game_button = ttk.Button(root, text="Stop Game", command=stop_game)
stop_game_button.pack()





root.mainloop()