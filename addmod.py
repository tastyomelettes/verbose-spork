#!/usr/bin/env python3

import os
import pickle

def get_initial_info():
    # Get Name and Workshop ID from user
    print('\n')
    name = input("Enter name: ")
    work_id = input("Enter workshop ID: ")
    return {'id': work_id, 'name': name}

def confirm_initial_info(info):
    print('\n')
    print("Name: " + info['name'])
    print("Workshop ID: " + info['id'])
    reply = input('\nAre you sure? (Y/N) ')
    if reply[:1].lower() == "y":
        return True
    elif reply[:1].lower() == "n":
        return False


### MAIN PROGRAM ###
os.system('clear')
print('DST Mod Tool v.0.0.1')
info = {}
while True:
    info = get_initial_info()
    if confirm_initial_info(info) == True:
        break
