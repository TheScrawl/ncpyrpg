# ncpyrpg
What will eventually, hopefully, be an ncurses python-based top down old school rpg engine for easy and fast rpg game development

We will see how far I actually get last time. 

## What does it do so far?
Newest to oldest changes
* lets a game designer to generate a game map in gamedata.py
* takes arrays and draws objects at given coordinates
* allows a player to move while colliding with objects that they shouldnt be able to move through

## Todos
* Sort out how im going to do the menu system (probably some sort of tab system)
* ~~Move things to a more "Engine-like" system that has more easily editable and expandable options for game creators.~~
* Add maps/rooms that link up
* Inventory system
* Stats system
* Combat system
* NPC system
* Shop system
* Quest System

## Started
* Add interactable objects in the world map (eg chests, monsters)
 
   * So far have a sort of button thing working, though it could theoretically do more
   * its a bit hacky, might redo once I figure out a better way of doing it
   * probably needs optimizing and whatnot
  
## Known issues (i.e cant be bothered trying to fix please dont ask)
* Lenny face ascii art doesnt work due to how the characters are handled. Not sure how to fix
* Many emoji do not work, due to being more than one character large
* due to use of eval() when i made map objects, could potentially lead to games being used for malicious purposes - though unlikely. I may redo how the map objects work in future to get rid of this issue, but at present i cbf
