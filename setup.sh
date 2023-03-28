#!/bin/bash
GIT_GAME_REPO=git@github.com:dinies/HexGame.git

# move into the game folder
# and clone the repo for the game

cd game
git clone $GIT_GAME_REPO

#TODO: 
# 1. tag a release on the game repo and use those
# 2. once we create docker/ folder with all dockerfiles probably
#     want to move this there