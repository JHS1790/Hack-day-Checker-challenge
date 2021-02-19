#!/usr/bin/python3

from colorama import Fore, Style
import json
import requests
import time


url = 'https://intranet.hbtn.io/'
api_key = 'f7f3415ad700490a7b94d2996061d774' #input("What is you API key? (In tools in the intranet) ")
user_email = '1646@holbertonschool.com' #input("What is your holberton email address? ")
user_pass = '2Tu4!Z&mPrKQ' #input("What is you intranet password? ") #We should see how to hide this if we have time
token_url = 'users/auth_token.json'
payload = {"api_key": api_key, "email": user_email, "password": user_pass, "scope": "checker"}
try:
    auth_response = requests.post(url + token_url, data=payload).json()
    auth_token = auth_response['auth_token']
except:
    print("Some of your details were incorrect, please double check them and try again.")
    exit()

project_id = input("What project would you like to check?\nPlease enter project id: ")
projects_request = requests.get(url + 'projects/' + project_id + '.json?auth_token=' + auth_token).json()
try:
    if projects_request['error']:
        print("Invalid project ID")
        exit()
except:
    pass

print(projects_request['name'])
for item in projects_request['tasks']:
    position = item['position'] 
    if position < 100:
        position -= 1
    print("\tTask {}: {}".format(position, item['title']))
    correction_request = requests.post(url + 'tasks/' + str(item['id']) + '/start_correction.json?auth_token=' + auth_token).json()
    try:
        if correction_request['error']:
            print('\t{}{}{}\n'.format(Fore.RED, correction_request['error'], Style.RESET_ALL))
            continue
    except:
        pass
    print("\tWaiting on checker...\n")

    while(True):
        time.sleep(5)
        correction = requests.get(url + 'correction_requests/' + str(correction_request['id']) + '.json?auth_token=' + auth_token).json()
        if correction['status'] == 'Done':
            i = 0
            for item in correction['result_display']['checks']:
                print("\t\t{} check {}: ".format(item['check_label'], i), end='')
                if item['passed'] == True:
                    print("{}Passed{}".format(Fore.GREEN, Style.RESET_ALL))
                else:
                    print("{}Failed{}".format(Fore.RED, Style.RESET_ALL))
                i += 1
            if correction['result_display']['all_passed'] == True:
                print("\tCongratulations All Checks Passed!\n")
            break
        elif correction['status'] == 'Fail':
            print("Checker Fail, post in #checkerisbroken")
            break

    #print(correction)
    #exit()
    
