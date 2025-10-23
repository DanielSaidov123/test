from random import randint
def create_card(rank:str, suite:str) -> dict:
    playing_cards={}
    try:
        x=int(rank)
        playing_cards["rank"]=rank
        playing_cards["suite"]=suite
        playing_cards["value"]=x


    except:
        if rank=="J":
            playing_cards["rank"]=rank
            playing_cards["suite"]=suite
            playing_cards["value"]=11
        if rank=="Q":
            playing_cards["rank"]=rank
            playing_cards["suite"]=suite
            playing_cards["value"]=12
        if rank=="K":
            playing_cards["rank"]=rank
            playing_cards["suite"]=suite
            playing_cards["value"]=13
        if rank=="A":
            playing_cards["rank"]=rank
            playing_cards["suite"]=suite
            playing_cards["value"]=14
    return playing_cards

# print(create_card("Q", "H")) 
# → {"rank": "10", "suite": "H", "value":10}

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"]>p2_card["value"]:
        return "p1"
    if p1_card["value"]==p2_card["value"]:
        return 'WAR'
    if p1_card["value"]<p2_card["value"]:
        return 'p2'
    
# print(compare_cards({"value": 5 }, {"value": 6 }))

def create_deck() -> list[dict]:
    playing_cards=[]
    for i in range(2,11):
        x=create_card(str(i),"S")
        playing_cards.append(x)
    
    for i in range(2,11):
        x=create_card(str(i),"D")
        playing_cards.append(x)

    for i in range(2,11):
        x=create_card(str(i),"C")
        playing_cards.append(x)

    for i in range(2,11):
        x=create_card(str(i),"H")
        playing_cards.append(x)

    x=create_card("J","H")
    playing_cards.append(x)
    x=create_card("J","C")
    playing_cards.append(x)
    x=create_card("J","D")
    playing_cards.append(x)
    x=create_card("J","S")
    playing_cards.append(x)

    x=create_card("Q","H")
    playing_cards.append(x)
    x=create_card("Q","C")
    playing_cards.append(x)
    x=create_card("Q","D")
    playing_cards.append(x)
    x=create_card("Q","S")
    playing_cards.append(x)

    x=create_card("K","H")
    playing_cards.append(x)
    x=create_card("K","C")
    playing_cards.append(x)
    x=create_card("K","D")
    playing_cards.append(x)
    x=create_card("K","S")
    playing_cards.append(x)

    x=create_card("A","H")
    playing_cards.append(x)
    x=create_card("A","C")
    playing_cards.append(x)
    x=create_card("A","D")
    playing_cards.append(x)
    x=create_card("A","S")
    playing_cards.append(x)

    return playing_cards


def shuffle(deck: list[dict]) -> list[dict]:
    for _ in range(0,1000):
        x=randint(0,51)
        y=randint(0,51)
        deck[x],deck[y]=deck[y],deck[x]
    return deck

print(shuffle(create_deck()))


       

                

    

                    

            
    