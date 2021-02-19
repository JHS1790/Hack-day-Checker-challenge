#!/usr/bin/python3

from colorama import Fore, Style
from getpass import getpass
import json
import requests
import time


"""This is all the information needed to make API calls to Holberton"""
url = 'https://intranet.hbtn.io/'
api_key = getpass("What is you API key? (In tools in the intranet) ")
user_email = input("What is your Holberton email address? ")
user_pass = getpass("What is you intranet password? ")
token_url = 'users/auth_token.json'
payload = {"api_key": api_key,
           "email": user_email,
           "password": user_pass,
           "scope": "checker"}

try:
    auth_response = requests.post(url + token_url, data=payload).json()
    auth_token = auth_response['auth_token']
except:
    print("Some of your details were incorrect.")
    print("Please double check them and try again.")
    exit()

"""
If we make a successful call to the intranet
next we will target a project to check
"""
project_id = input("What project would you like to check?\nPlease enter project id: ")
projects_request = requests.get(url + 'projects/' +
                                project_id + '.json?auth_token=' +
                                auth_token).json()

try:
    if projects_request['error']:
        print("Invalid project ID")
        exit()
except:
    pass

"""
With a succesful project specific API call we can access
all the details and run checker
"""
print(projects_request['name'])
for item in projects_request['tasks']:
    position = item['position']
    if position < 100:
        position -= 1
    print("\tTask {}: {}".format(position, item['title']))
    """
    Correction_Request will establish a connection to checked
    to get us the ids we need to run checker
    """
    correction_request = requests.post(url + 'tasks/' +
                                       str(item['id']) +
                                       '/start_correction.json?auth_token=' +
                                       auth_token).json()

    try:
        if correction_request['error']:
            print('\t{}{}{}\n'.format(Fore.RED,
                                      correction_request['error'],
                                      Style.RESET_ALL))
            continue
    except:
        pass
    print("\tWaiting on checker...")

    """
    We have an infinite while loop to wait for checker
    to be done with each task before moving on
    """
    while(True):
        time.sleep(10)
        correction = requests.get(url +
                                  'correction_requests/' +
                                  str(correction_request['id']) +
                                  '.json?auth_token=' +
                                  auth_token).json()
        if correction['status'] == 'Done':
            """
            Once we have a done for a task we will
            print out the checks as Passed or Failed
            """
            i = 0
            for item in correction['result_display']['checks']:
                print("\t\t{} check {}: ".format(item['check_label'], i),
                      end='')
                if item['passed'] is True:
                    print("{}Passed{}".format(Fore.GREEN, Style.RESET_ALL))
                else:
                    print("{}Failed{}".format(Fore.RED, Style.RESET_ALL))
                i += 1
            if correction['result_display']['all_passed'] is True:
                print("\tCongratulations All Checks Passed!\n")
            break
        elif correction['status'] == 'Fail':
            print("Checker Fail, post in #checkerisbroken\n")
            break
