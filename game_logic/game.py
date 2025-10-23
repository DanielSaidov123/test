from utils.deck import *
def create_player(name:str="AI") -> dict:
    players={}
    if name:
        players["name"]=name
    else:
        players["name"]="AI"
    players["hand"]=[]
    players["won_pile"]=[]
    return players

# print(create_player("daniel"))

def init_game() -> dict :
    name1=create_player("daniel")
    name2=create_player()
    deck=shuffle(create_deck())
    for i in range(26):
        name1["hand"].append(deck[i])
    for i in range(26,50):
        name2["hand"].append(deck[i])
    
    return {"deck":deck,"player_1":name1,"player_2":name2}

print(init_game())
def play_round(player_1: dict, player_2: dict)-> None:
    x=compare_cards(player_1,player_2)
    y=player_1[2]
    if x=="p1":
        player_1["won_pile"].append(player_2["hand"][0])
        player_1["won_pile"].append(player_2["hand"][0])
        player_2["hand"].pop(0)

    if x=="p2":
        player_1["won_pile"].append(player_1["hand"][0])
        player_1["won_pile"].append(player_1["hand"][0])








    
    




