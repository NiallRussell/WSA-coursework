import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(url)
deck = response.json()
deck_id = deck["deck_id"]

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url)
cards = draw_response.json()["cards"]

for card in cards:
    print(f"{card['value']} of {card['suit']}")