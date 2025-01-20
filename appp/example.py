import requests

r = requests.get("http://127.0.0.1:8000/hotel/4/room/5", 
                 params={
                     "date_from": "today", 
                     "date_to": "tomorrow", 
                     "room_name": "Deluxe"})

print(r.json())