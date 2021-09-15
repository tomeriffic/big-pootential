from math import exp
from typing import List
import random
import time

END_GAME = "Poo"

class Card:
    def __init__(self, name: str, size: int, rigidity: int, special_ability = None):
        self.name = name
        self.size = size
        self.rigidity = rigidity
        self.special_ability = special_ability

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def add_to_deck(self, card: Card):
        self.cards.append(card)

    def pop_from_deck(self) -> Card:
        card = self.cards.pop()
        return card
    
    def initialize_deck(self) -> None:
        card_specifications = [
            { "name": "Vindaloo", "size": 2, "rigidity": -1 },
            { "name": "Vindaloo", "size": 2, "rigidity": -1 },
            { "name": "Bad Bucket of Chicken", "size": 5, "rigidity": 2 },
            { "name": "Bad Bucket of Chicken", "size": 5, "rigidity": 2 },
            { "name": "Chow Mein", "size": 1, "rigidity": -2 },
            { "name": "Chow Mein", "size": 1, "rigidity": -2 },
            { "name": "Canned Prunes", "size": 1, "rigidity": 4 },
            { "name": "Canned Prunes", "size": 1, "rigidity": 4 },
            { "name": "Burger and Chips", "size": 1, "rigidity": -1 },
            { "name": "Burger and Chips", "size": 1, "rigidity": -1 },
            { "name": "Mommas Homemade Cooking", "size": 1, "rigidity": 1 },
            { "name": "Mommas Homemade Cooking", "size": 1, "rigidity": 1 },
            { "name": "Fruit Salad", "size": 1, "rigidity": 3 },
            { "name": "Fruit Salad", "size": 1, "rigidity": 3 },
            { "name": "Full English", "size": 2, "rigidity": 2 },
            { "name": "Full English", "size": 2, "rigidity": 2 },
            { "name": "Burrito Grande", "size": 2, "rigidity": -1 },
            { "name": "Burrito Grande", "size": 2, "rigidity": -1 },
            { "name": "Chicken Fajita", "size": 2, "rigidity": -1 },
            { "name": "Chicken Fajita", "size": 2, "rigidity": -1 },
            { "name": "Chili", "size": 1, "rigidity": -2 },
            { "name": "Chili", "size": 1, "rigidity": -2 },
            { "name": "Avocado on Toast", "size": 1, "rigidity": 1 },
            { "name": "Avocado on Toast", "size": 1, "rigidity": 1 },
            { "name": "Turkey Dinosaurs with Beans", "size": 2, "rigidity": 1 },
            { "name": "Turkey Dinosaurs with Beans", "size": 2, "rigidity": 1 },
            { "name": "Anchovy Pizza", "size": 1, "rigidity": 1 },
            { "name": "Anchovy Pizza", "size": 1, "rigidity": 1 },
            { "name": "Sugar Free Mints", "size": 1, "rigidity": -3 },
            { "name": "Sugar Free Mints", "size": 1, "rigidity": -3 },
            { "name": "Doner Kebab", "size": 3, "rigidity": -1 },
            { "name": "Doner Kebab", "size": 3, "rigidity": -1 },
            { "name": "Meal Deal", "size": 2, "rigidity": 2 },
            { "name": "Meal Deal", "size": 2, "rigidity": 2 },
            { "name": "Pint", "size": 0, "rigidity": -1 },
            { "name": "Pint", "size": 0, "rigidity": -1 },
            { "name": "Coffee", "size": 0, "rigidity": -3 },
            { "name": "Coffee", "size": 0, "rigidity": -3 },
            { "name": "Tea", "size": 0, "rigidity": -1 },
            { "name": "Tea", "size": 0, "rigidity": -1 },
            { "name": "Shot of Baked Bean Juice", "size": 0, "rigidity": 1 },
            { "name": "Shot of Baked Bean Juice", "size": 0, "rigidity": 1 },
            { "name": "RELEASE!", "size": 0, "rigidity":0, "Special Ability": END_GAME },
            { "name": "RELEASE!", "size": 0, "rigidity":0, "Special Ability": END_GAME },
            { "name": "RELEASE!", "size": 0, "rigidity":0, "Special Ability": END_GAME },
            { "name": "RELEASE!", "size": 0, "rigidity":0, "Special Ability": END_GAME },
            { "name": "LAXATIVE!", "size": 0, "rigidity":0, "Special Ability": "Discard 5" },
            { "name": "LAXATIVE!", "size": 0, "rigidity":0, "Special Ability": "Discard 5" },
            { "name": "PREMATURE POO!", "size": 0, "rigidity":0, "Special Ability": "Discard 3" },
            { "name": "PREMATURE POO!", "size": 0, "rigidity":0, "Special Ability": "Discard 3" },
            { "name": "DISAGREEMENT WITH THE BOWELS!", "size": 0, "rigidity":0, "Special Ability": "Discard 1" },
            { "name": "DISAGREEMENT WITH THE BOWELS!", "size": 0, "rigidity":0, "Special Ability": "Discard 1" }
        ]

        for card in card_specifications:
            card = Card(card.get("name"), card.get("size"), card.get('rigidity'), card.get("Special Ability"))
            self.add_to_deck(card)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards_in_hand = []
        self.is_human = True
        if "CPU" in self.name:
            self.is_human = False

    def draw_from_deck(self, deck: Deck) -> Card:
        card = deck.pop_from_deck()
        self.cards_in_hand.append(card)
        return card

    def discard(self, count: int) -> List[Card]:
        discard_cards = []
        count = count + 1 # HACK: This is because it needs to rid of the discard card also
        try:
            for i in range(count):
                card = self.cards_in_hand.pop()
                discard_cards.append(card)
        except Exception:
            print("WARNING: Not enough cards to discard")
        return discard_cards

def main():
    players = []
    p1_name = input("Enter Your Name: ")
    player1 = Player(p1_name)
    playerCPU = Player("CPU")

    deck = Deck()
    deck.shuffle()
    print("Deck Setup and Shuffle Done!")


    print("Filp a Coin to Start...")
    user = input("'h' for Heads, 't' for Tails: ")
    coin = 'h' if random.randint(0,1) == 0 else "t" # Coin, 0 Heads, 1 Tails
    print(f"Coin is... {coin}")
    
    starts = None
    if user == coin:
        print(f"{player1.name} Starts.")
        players.append(player1)
        players.append(playerCPU)
    else:
        print("CPU Starts.")
        players.append(playerCPU)
        players.append(player1)
    

    is_game_on = True
    turn_number = 0
    next_player = 0
    while is_game_on:
        print(f"Turn Number: {turn_number}")

        print(f"{players[next_player].name} turn next.")

        if players[next_player].is_human:
            # User Input
            to_draw = input("Press 'd' to Draw from Deck. 'e' to exit: ")

            if to_draw == "d":
                card = players[next_player].draw_from_deck(deck)
                print(f"You picked up: {card.name}, Size: {card.size}, Rigidity {card.rigidity}, Special Ability {card.special_ability}")
                time.sleep(1.5)

                if card.special_ability is not None:
                    print(f"Activating Special Ability: {card.special_ability}")
                    time.sleep(1.5)

                    if "Discard" in card.special_ability:
                        print(f"{players[next_player].name} Discarding...")
                        discard_count = int(card.special_ability.replace("Discard ", ""))
                        players[next_player].discard(discard_count)

                    if card.special_ability == END_GAME:
                        print(f"{players[next_player].name} POO'D HIMSELF, MWUHAHAHA")
                        break

            elif to_draw == "e":
                is_game_on = False
                break

        else:
            print(f"{players[next_player].name} has Draw from Deck")
            hidden_card = players[next_player].draw_from_deck(deck)

            if hidden_card.special_ability is not None:
                print(f"Activating Special Ability: {hidden_card.special_ability}")
                time.sleep(1.5)

                if "Discard" in hidden_card.special_ability:
                    print(f"{players[next_player].name} Discarding...")
                    discard_count = int(hidden_card.special_ability.replace("Discard ", ""))
                    players[next_player].discard(discard_count)

                if hidden_card.special_ability == END_GAME:
                    print(f"{players[next_player].name} POO'D HIMSELF, MWUHAHAHA")
                    break


        turn_number = turn_number + 1
        next_player = turn_number % (len(players))

    

    print("---Start of Report---")
    for player in players:
        print(player.name)
        print("Cards in Hand")
        for card in player.cards_in_hand:
            print(f"- {card.name}")

    print("---Scores---")
    for player in players:
        size = 0
        rigidity = 0
        for card in player.cards_in_hand:
            size += card.size
            rigidity += card.rigidity
        print(f"{player.name} Scored Size {size}, and Rigidity {rigidity}")


if __name__ == "__main__":
    main()
