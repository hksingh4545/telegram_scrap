#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import configparser
import os, sys
import csv
import random
from time import sleep
import traceback

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME  = [10, 5, 15, 12, 8, 21, 11, 13, 14, 16, 3]


class main():

    def banner():
        
        print(f"""
    {re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
    {re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
    {re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

                version : 3.1
            youtube.com/theunknon
            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] run python3 setup.py first !!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Enter the code: '+re))
        
        os.system('clear')
        main.banner()
        input_file = sys.argv[1]
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f,delimiter=",",lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['username'] = row[0]
                user['id'] = int(row[1])
                user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)
        print(gr+"[1] send sms by user ID\n[2] send sms by username ")
        mode = int(input(gr+"Input : "+re))
         
        message = input(gr+"[+] Enter Your Message : "+re)
        n = 0 
        for user in users:
            n += 1
            if n % 50 == 0:
                sleep(300)
            try:
                print ("Adding {}".format(user['id']))
                if mode == 1:
                    if user['username'] == "":
                        continue
                    receiver = client.get_input_entity(user['username'])
                elif mode == 2:
                    receiver = InputPeerUser(user['id'], user['access_hash'])
                else:
                    sys.exit("Invalid Mode Selected. Please Try Again.")
                    client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                    print("Waiting for 60-180 Seconds...")
                    time.sleep(random.randrange(60, 180))
            except PeerFloodError:
                print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            except UserPrivacyRestrictedError:
                print("The user's privacy settings do not allow you to do this. Skipping.")
            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue

        client.disconnect()
        print("Done. Message sent to all users.")



main.send_sms()
