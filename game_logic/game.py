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

def play_round(player_1: dict, player_2: dict)-> None:
    x=player_1["hand"].pop()
    y=player_1["hand"].pop()
    z=compare_cards(x,y)
    if z=="p1":
        player_1["won_pile"].append(x)
        player_1["won_pile"].append(y)

    if z=="p2":
        player_1["won_pile"].append(x)
        player_1["won_pile"].append(y)








    
    




