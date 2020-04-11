import requests
import json

response = requests.get("https://api.chess.com/pub/player/dbutsalt/stats")
json_data = json.loads(response.text)

wins = json_data['chess_blitz']['record']['win']
losses = json_data['chess_blitz']['record']['loss']
draws = json_data['chess_blitz']['record']['draw']

print("Wins: " +str(wins))
print("Losses: " +str(losses))
print("Draws: " +str(draws))