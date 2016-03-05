#!/usr/bin/env sh

sudo easy_install pip
sudo pip install virtualenv
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
