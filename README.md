# InstaWaves
This repository contains a code for Telegram bot which allows people to promote their Instagram accounts.
The idea is simple. Telegram group or chat has admin user which moderates it. People can register for so-called waves. If you register for a wave, you should like and comment on the last post of all other attendees.
# Wave states
register state - users register for wave <br>
bidding state - users like and comment each other post<br>
assuring state - bot ensures that everybody completed rules of liking and commenting<br.
finished state - wave is finished. A new wave can be created<br>
Admin user moderates the transition between wave states
# Additional logic
There is "privilege" functionality. Admin can make the user privileged. In this case, the user can stop liking and commenting on other posts.
# Instagram scraping credits
The most credit for Instagram scraping logic should be given to @OlegYurchik. 
https://github.com/OlegYurchik/pyInstagram - this is a repository which was the starting point for scraping functionality implementation.
#Usage
You can use this code, as you wish. I don't want to improve this project. You can automate wave processes, implement a decent payment system or just get rid of things like consts.py files, etc.
If you can make some money on this, I would appreciate if you contact me, but that's definitely not obligatory.
Initially, this project was made for one of my clients, but he appeared to be not the most pleasant one. Paolo, if you are reading this, you are a complete douche.
Please don't worry about stuff like API keys or something like that. It can't harm anyone.
