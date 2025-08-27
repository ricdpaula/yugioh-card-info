from main import app
import requests
from flask import render_template, request

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/data/")
def get_card():
    url_base = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="
    if request.args.get('card_name') != "":
        response = requests.get(url_base + request.args.get('card_name'))
    else:
        return render_template("card.html", card_name=False)
    if response.status_code == 200:
        data = response.json()
        if data["data"][0]["frameType"] == "normal" or data["data"][0]["frameType"] == "effect" or data["data"][0]["frameType"] == "ritual" or data["data"][0]["frameType"] == "xyz" or data["data"][0]["frameType"] == "synchro" or data["data"][0]["frameType"] == "link": 
            card_img = data["data"][0]["card_images"][0]["image_url"]
            card_name = data["data"][0]["name"]
            card_atk = data["data"][0]["atk"]
            card_def = data["data"][0]["def"]
            card_description = data["data"][0]["desc"]
            card_level = data["data"][0]["level"]
            card_race = data["data"][0]["race"]
            card_type = data["data"][0]["type"]
            card_attribute = data["data"][0]["attribute"]
            card_frameType = data["data"][0]["frameType"]
            return render_template("card.html", image=card_img, name=card_name, attack=card_atk, defense=card_def, desc=card_description, level=card_level, race=card_race, type=card_type, attribute=card_attribute, frameType=card_frameType)
        else:
            card_img = data["data"][0]["card_images"][0]["image_url"]
            card_name = data["data"][0]["name"]
            card_description = data["data"][0]["desc"]
            card_race = data["data"][0]["race"]
            card_type = data["data"][0]["type"]
            card_frameType = data["data"][0]["frameType"]
            return render_template("card.html", image=card_img, name=card_name, desc=card_description, race=card_race, type=card_type, frameType=card_frameType)
    
    elif response.status_code == 400:
        return render_template("card.html", er_cardNotFound="This card not found")
