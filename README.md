# ncpyrpg
What will eventually, hopefully, be an ncurses python-based top down old school rpg engine for easy and fast rpg game development

We will see how far I actually get this time. 

## What does it do so far?
Newest to oldest changes
* allows output to the menu window from mapObjects
* user can create mapObjects, interactive characters that do things when stepped on
* lets a game designer to generate a game map in gamedata.py
* takes arrays and draws objects at given coordinates
* allows a player to move while colliding with objects that they shouldnt be able to move through

## How do I use it?
See the [Wiki](https://github.com/TheScrawl/ncpyrpg/wiki)

## Todos
* Sort out how im going to do the menu system (probably some sort of tab system)
* Add maps/rooms that link up
* Inventory system
* Stats system
* Combat system
* NPC system
* Shop system
* Quest System
* Simplify the game making system

## Started
* Add interactable objects in the world map (eg chests, monsters)
    * mostly working, any futher changes/additions will need a more fleshed out menu system

## Known issues (i.e cant be bothered trying to fix please dont ask)
* Lenny face ascii art doesnt work due to how the characters are handled. Not sure how to fix
* Many emoji do not work, due to being more than one character large
* due to use of eval() when i made map objects, could potentially lead to games being used for malicious purposes - though unlikely. I may redo how the map objects work in future to get rid of this issue, but at present i cbf
