# Pocket Kitchen User Interface
Pocket Kitchen is a system for managing food more efficiently in the home towards reducing household food waste. This is a Node app structured for deployment in Heroku. It is a user-interface for the Pocket Kitchen app, which tracks incoming and outgoing food items through the Pocket Kitchen API on the Raspberry Pi. As well as this, it pulls the inventory from a MongoDB datbase, tracks expiry dates, provides recipe suggestions and alerts for items approaching expiry.

- **Expiry-tracking** - When new items are added to the inventory, the user is prompted to enter an expiry date. The app then tracks the expiry date and alerts the user when items are approaching expiry.
- **Recipe suggestions** - The app provides recipe suggestions based on preventing items in the inventory expiring. The user can also search for recipes which use the most stocked ingredients.
- **Alerts** - The app alerts the user when items are approaching expiry, and when items are expiring on the current day.

<img src="https://github.com/myPocketKitchen/PocketKitchen-UI/assets/79009541/f18fc059-9c5b-4132-b274-dc63f9969a0f" height=600>

## Getting Started
 
```
pip install requirements.txt
```

## System Architecture
This web app is part of a wider system architecture for food management. The system architecture is as follows:

<img src="https://github.com/myPocketKitchen/PocketKitchen-UI/assets/79009541/03515908-76ee-4cad-85e6-618a7b82cd76" width=600>

## Web App Flow Chart

<img src="https://github.com/mimireyburn/LLMyWeather/assets/79009541/ff5e79e3-06a6-47bd-a45f-6c68bfd9cc1b" height=600>

