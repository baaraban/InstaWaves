# InstaWaves
This repository contains a code for Telegram bot which allows people to promote their Instagram accounts.<br>
The idea is simple. Telegram group or chat has admin user which moderates it. People can register for so-called waves. <br>
If you register for a wave, you should like and comment on the last post of all other attendees.
# Wave states
register state - users register for wave <br>
bidding state - bot sends message with links to all posts which should be liked and commented on<br>
assuring state - bot ensures that everybody completed rules of liking and commenting<br>
finished state - wave is finished. A new wave can be created<br>
Admin user moderates the transition between wave states
# Additional logic
There is "privilege" functionality. Admin can make the user privileged. In this case, the user can stop liking and commenting on other posts.
# Instagram scraping credits
The most credit for Instagram scraping logic should be given to @OlegYurchik. <br>
https://github.com/OlegYurchik/pyInstagram - this is a repository which was the starting point for scraping functionality implementation.
